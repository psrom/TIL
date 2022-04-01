# !pip install transformers
# ------------------------------------------------------------------------
# BERT를 이용한 네이버 영화 감성분석
import pandas as pd
import numpy as np
import tensorflow as tf
from transformers import BertTokenizer, TFBertModel
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint
import re
from tqdm.auto import tqdm
import matplotlib.pyplot as plt
import os
# ------------------------------------------------------------------------
DATA_PATH = '/content/drive/MyDrive/DATA/'

# DATA_PATH 아래 kykim_bert 폴더를 만들어 놓는다.
ckpt_path = DATA_PATH + 'kykim_bert/weights.h5'

# huggingface.co --> (우측상단) models --> (왼쪽 메뉴) languages에서 ko --> (오른쪽) kykim/bert-kor-base 클릭
tokenizer = BertTokenizer.from_pretrained("kykim/bert-kor-base", 
                                          cache_dir = 'kykim_bert_ckpt', 
                                          do_lower_case=False)
word2idx = tokenizer.vocab
idx2word = {v:k for k, v in word2idx.items()}

df = pd.read_csv(DATA_PATH + 'naver_movie/ratings.txt', header=0, delimiter='\t', quoting=3)[:10]
df = df.dropna()

# 간단한 전처리. 한글이 아닌 숫자, 영문자, 기호 등은 공백문자로 치환.
df['document'] = df['document'].apply(lambda x: re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\s]", " ", x))
df.drop('id', axis = 1, inplace = True)

document = list(df['document'])
label = list(df['label'])
x_train, x_test, y_train, y_test = train_test_split(document, label, test_size=0.2)
# ------------------------------------------------------------------------
MAX_LEN = 60
# ------------------------------------------------------------------------
# Bert Tokenizer
def bert_tokenizer(sent):
    
    encoded_dict = tokenizer.encode_plus(
        text = sent,
        add_special_tokens = True,      # Add '[CLS]' and '[SEP]'
        max_length = MAX_LEN,           # Pad & truncate all sentences.
        padding = 'max_length',
        # pad_to_max_length = True,
        return_attention_mask = True,   # Construct attn. masks.
        truncation = True
    )
    
    input_id = encoded_dict['input_ids']
    attention_mask = encoded_dict['attention_mask'] # And its attention mask (simply differentiates padding from non-padding).
    token_type_id = encoded_dict['token_type_ids']  # differentiate two sentences
    
    return input_id, attention_mask, token_type_id
# ------------------------------------------------------------------------
text = document[1]
id, mask, typ = bert_tokenizer(text)
print(text)
print(id)
print(mask)
print(typ)

text_1 = [idx2word[x] for x in id]
print(text_1)

# 문장 복원
print((' '.join(text_1)).replace(' ##', ''))  # 원리
print(tokenizer.decode(id))

print('토큰 길이 =', len(id))
# ------------------------------------------------------------------------
def build_data(doc):
    x_ids = []
    x_msk = []
    x_typ = []

    for sent in tqdm(doc):
        input_id, attention_mask, token_type_id = bert_tokenizer(sent)
        x_ids.append(input_id)
        x_msk.append(attention_mask)
        x_typ.append(token_type_id)

    x_ids = np.array(x_ids, dtype=int)
    x_msk = np.array(x_msk, dtype=int)
    x_typ = np.array(x_typ, dtype=int)

    return x_ids, x_msk, x_typ
# ------------------------------------------------------------------------
x_train_ids, x_train_msk, x_train_typ = build_data(x_train)
x_test_ids, x_test_msk, x_test_typ = build_data(x_test)

y_train = np.array(y_train).reshape(-1, 1)
y_test = np.array(y_test).reshape(-1, 1)

x_train_ids.shape, y_train.shape
x_test_ids.shape, y_test.shape
# ------------------------------------------------------------------------
bert_model = TFBertModel.from_pretrained("kykim/bert-kor-base", cache_dir = 'kykim_bert_ckpt')
bert_model.summary() # bert_model을 확인한다. trainable params = 177,854,978
# ------------------------------------------------------------------------
# BERT 입력
# ---------
x_input_ids = Input(batch_shape = (None, MAX_LEN), dtype = tf.int32)
x_input_msk = Input(batch_shape = (None, MAX_LEN), dtype = tf.int32)
x_input_typ = Input(batch_shape = (None, MAX_LEN), dtype = tf.int32)

# BERT 출력
# ---------
output_bert = bert_model([x_input_ids, x_input_msk, x_input_typ])[1]

# Downstream task : 네이버 영화 감성분석
# -------------------------------------
y_output = Dense(1, activation = 'sigmoid')(output_bert)
model = Model([x_input_ids, x_input_msk, x_input_typ], y_output)
model.compile(loss = 'binary_crossentropy', optimizer = Adam(learning_rate = 0.01))
model.summary()
# ------------------------------------------------------------------------
if os.path.exists(ckpt_path):
    model.load_weights(ckpt_path)
    print('학습된 weight가 적용됐습니다.')

# Create a callback that saves the model's weights, every epochs
cp_callback = ModelCheckpoint(filepath=ckpt_path, 
                              save_weights_only=True, 
                              verbose=1,
                              save_freq=1)

x_train = [x_train_ids, x_train_msk, x_train_typ]
x_test = [x_test_ids, x_test_msk, x_test_typ]
hist = model.fit(x_train, y_train, 
                 validation_data = (x_test, y_test), 
                 epochs=3, 
                 batch_size=1024,
                 callbacks=[cp_callback])
# ------------------------------------------------------------------------
# Loss history를 그린다
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss history")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 시험 데이터로 학습 성능을 평가한다
pred = model.predict(x_test)
y_pred = np.where(pred > 0.5, 1, 0)
accuracy = (y_pred == y_test).mean()
print("\nAccuracy = %.2f %s" % (accuracy * 100, '%'))