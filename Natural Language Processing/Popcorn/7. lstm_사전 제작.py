# Word Embedding & LSTM 이용 감성분석
# word2idx 갯수 줄여서 제작
from msilib.schema import _Validation_records
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pickle
# ======================================================
DATA_PATH = '/content/drive/MyDrive/DATA/movie/'
# 학습 데이터 불러오기
with open(DATA_PATH + 'popcorn.pkl', 'rb') as f:
    x_text, _, y_target, _ = pickle.load(f)

y_target = np.array(y_target).reshape(-1, 1)

# ======================================================
# 사전 크기 축소
VOCAB_SIZE = 10000
tokenizer = Tokenizer(num_words = VOCAB_SIZE, oov_token = '<OOV>')
tokenizer.fit_on_texts(x_text) # 사용 빈도 기반으로 사전 제작
x_feat = tokenizer.texts_to_sequences(x_text)
tokenizer.word_index['<PAD>']=0

word2idx = {k:v for k, v in tokenizer.word_index.items() if v < VOCAB_SIZE}
# 전체 사전 word_index는 5만개이지만 그중에서 빈도가 높은 VOCAB_SIZE만큼만 가져와서 사전을 다시 만든다.

# ======================================================
MAX_SEQ_LEN = 174
x_data_pad = pad_sequneces(x_feat, maxlen=MAX_SEQ_LEN, padding='post', truncating='post')

# ======================================================
# 학습 데이터와 시험 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(x_data_pad, y_target, test_size=0.2)

# ======================================================
# Embedding & LSTM 모델 생성
vocab_size = len(word2idx)
EMBEDDING_DIM = 32
HIDDEN_DIM = 64

x_input = Input(batch_shape=(None, x_train.shape[1]))
e_layer = Embedding(input_dim=vocab_size, output_dim=EMBEDDING_DIM)(x_input)
e_layer = Dropout(rate=0.5)(e_layer)
r_layer = LSTM(HIDDEN_DIM, dropout=0.5)(e_layer)
y_output = Dense(1, activation='sigmoid')(r_layer)

model = Model(x_input, y_output)
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0001))
model.summary

# ======================================================
# 학습
hist = model.fit(x_train, y_train, _Validation_data = (x_test, y_test), batch_size=1024, epochs=50)

# ======================================================
# Loss history
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label='Test loss')
plt.legend()
plt.title('loss history')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# ======================================================
# 시험 데이터로 학습 성능 평가
pred = model.predict(x_test)
y_pred = np.where(pred>0.5, 1, 0)
accuracy = (y_pred == y_test).mean()
print('\nAccuracy = %.2f %s' % (accuracy * 100, '%'))