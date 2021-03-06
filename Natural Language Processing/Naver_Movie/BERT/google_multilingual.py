# !pip install transformers
# ------------------------------------------------------------------------
import pandas as pd
import numpy as np
import tensorflow as tf
from transformers import BertTokenizer, TFBertModel
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import re
import pickle
from tqdm.auto import tqdm
import matplotlib.pyplot as plt
# ------------------------------------------------------------------------
tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased", cache_dir='bert_ckpt', do_lower_case=False)
word2idx = tokenizer.vocab
idx2word = {v:k for k, v in word2idx.items()}

enc = tokenizer.encode('I love you'.split())
print(enc)
print([idx2word[x] for x in enc])

dec = tokenizer.decode(enc)
print(dec)
# ------------------------------------------------------------------------
DATA_PATH = '/content/drive/MyDrive/DATA/'
df = pd.read_csv(DATA_PATH + 'naver_movie/ratings.txt', header=0, delimiter='\t', quoting=3)
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

    for sent in tqdm(doc, total=len(doc)):
        input_id, attention_mask, token_type_id = bert_tokenizer(sent)
        x_ids.append(input_id)
        x_msk.append(attention_mask)
        x_typ.append(token_type_id)

    x_ids = np.array(x_ids, dtype=int)
    x_msk = np.array(x_msk, dtype=int)
    x_typ = np.array(x_typ, dtype=int)

    return x_ids, x_msk, x_typ

x_train_ids, x_train_msk, x_train_typ = build_data(x_train)
x_test_ids, x_test_msk, x_test_typ = build_data(x_test)

y_train = np.array(y_train).reshape(-1, 1)
y_test = np.array(y_test).reshape(-1, 1)

x_train_ids.shape, y_train.shape
x_test_ids.shape, y_test.shape

bert_model = TFBertModel.from_pretrained("bert-base-multilingual-cased", cache_dir='bert_ckpt')
bert_model.summary() # bert_model을 확인한다. trainable params = 177,854,978

# 시간이 오래 걸리므로 bert_model의 fine-tuning을 잠시 막아 놓자.
# downstream task 학습을 위해 bert_model도 fine-tuning해야 한다.
bert_model.trainable = False
bert_model.summary() # bert_model을 다시 확인한다. trainable params = 0

# BERT 입력
# ---------
x_input_ids = Input(batch_shape = (None, MAX_LEN), dtype = tf.int32)
x_input_msk = Input(batch_shape = (None, MAX_LEN), dtype = tf.int32)
x_input_typ = Input(batch_shape = (None, MAX_LEN), dtype = tf.int32)

# BERT 출력
# [0]: (None, 60, 768) - sequence_output, [1]: (None, 768) - pooled_output
# ------------------------------------------------------------------------
output_bert = bert_model([x_input_ids, x_input_msk, x_input_typ])[0]
# ------------------------------------------------------------------------
# FNN 모델
# output_bert = bert_model([x_input_ids, x_input_msk, x_input_typ])[1]
# y_output = Dense(1, activation = 'sigmoid')(output_bert)
# model = Model([x_input_ids, x_input_msk, x_input_typ], y_output)
# model.compile(loss = 'binary_crossentropy', optimizer = Adam(learning_rate = 0.01))
# model.summary()
# ------------------------------------------------------------------------

# Downstream task : 네이버 영화 감성분석
# ------------------------------------------------------------------------
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Conv1D, GlobalMaxPool1D, Concatenate
from tensorflow.keras import regularizers

VOCAB_SIZE = len(word2idx)
EMB_SIZE = 32
NUM_FILTER = 16

# Convolution & Pooling
def conv1d_maxpool(x, k):
    conv = Conv1D(filters=NUM_FILTER, kernel_size=k, 
                  activation='relu',
                  padding='same',
                  kernel_regularizer=regularizers.l2(0.01))(x)
    conv = Dropout(rate=0.5)(conv)
    return GlobalMaxPool1D()(conv)

h_pool = [conv1d_maxpool(output_bert, k=i) for i in [3, 4]]
h_concat = Concatenate()(h_pool)
y_output = Dense(1, activation='sigmoid')(h_concat)

model = Model([x_input_ids, x_input_msk, x_input_typ], y_output)
model.compile(loss = 'binary_crossentropy', optimizer = Adam(learning_rate = 0.01))
model.summary()
# ------------------------------------------------------------------------
# output_bert
# ------------------------------------------------------------------------
x_train = [x_train_ids, x_train_msk, x_train_typ]
x_test = [x_test_ids, x_test_msk, x_test_typ]
hist = model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs=3, batch_size=1024)
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