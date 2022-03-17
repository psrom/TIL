# Word Embedding & LSTM을 이용한 감성 분석
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
    _, x_feat, y_target, word2idx = pickle.load(f)
# lstm을 이용하기 위해서는 단어를 수치화 시킨 값이 필요해서 word2idx를 가져온다.

# ======================================================
y_target = np.array(y_target).reshape(-1, 1)

# 각 리뷰의 길이를 max_seq_len으로 맞추기
# 길면 자르고, 짧으면 padding 추가
MAX_SEQ_LEN = 174
x_data_pad = pad_sequences(x_feat, maxlen=MAX_SEQ_LEN, padding='post', truncating='post')

# ======================================================
# 학습 데이터와 시험 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(x_data_pad, y_target, test_size=0.2)
# x_train.shape, x_test.shape, y_train.shape, y_test.shape
# ((20000, 174), (5000, 174), (20000, 1), (50000, 1))
vocab_size = len(word2idx)

# ======================================================
# Embedding & LSTM 모델 생성
# Embedding을 사용하는 이유: 1) one-hot-encoding 2) 사전의 갯수 만큼 수치 벡터로 바꿔줄 수 있다 3) 행렬 계산 없이 lookup process(속도 빠름)
# LSTM을 사용하는 이유: 1) 데이터 유실 없이 사용 2) sequence 분석 가능
# RNN은 Gradient Vanishing 현상 때문에 잘 안 쓰고 대신 LSTM을 사용
EMBEDDING_DIM = 32
HIDDEN_DIM = 64

x_input = Input(batch_shape=(None, x_train.shape[1]))
e_layer = Embedding(input_dim=vocab_size, output_dim=EMBEDDING_DIM)(x_input) # 단어 의미가 반영된 수치
e_layer= Dropout(rate=0.5)(e_layer)
r_layer = LSTM(HIDDEN_DIM, dropout=0.5)(e_layer)
y_output = Dense(1, activation='sigmoid')(r_layer)

model = Model(x_input, y_output)
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0001))
model.summary()

# ======================================================
# 학습
hist = model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=1024, epochs=50)

# ======================================================
# Loss History 그리기
plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label='Test loss')
plt.legend()
plt.title('Loss history')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# ======================================================
# 시험 데이터로 학습 성능 평가
pred = model.predict(x_test)
y_pred = np.where(pred > 0.5, 1, 0) # 0.5이상이면 1, 0.5 미만이면 0으로 돌려줌
accuracy = (y_pred == y_test).mean()
print('\nAccuracy = %.2f %s' % (accuracy * 100, '%'))