# Word Embedding & CNN을 이용한 감성분석
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout
from tensorflow.keras.layers import Conv1D, GlobalMaxPool1D, Concatenate
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers
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
VOCAB_SIZE = 20000
tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token='<OOV>')
tokenizer.fit_on_texts(x_text)
x_feat = tokenizer.texts_to_sequences(x_text)
word2idx = {k:v for k, v in tokenizer.word_index.items() if v < VOCAB_SIZE}
word2idx['<PAD>'] = 0

# ======================================================
# 리뷰 길이 max_seq_len으로 맞추기
MAX_SEQ_LEN = 174
x_data_pad = pad_sequences(x_feat, maxlen=MAX_SEQ_LEN, padding='post', truncating='post')

# ======================================================
# 학습 데이터와 시험 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(x_data_pad, y_target, test_size=0.2)

# ======================================================
# CNN 모델 생성
VOCAB_SIZE = len(word2idx)
EMB_SIZE = 32
NUM_FILTER = 32

# Convolution & Pooling
def conv1d_maxpool(x, k):
    conv = Conv1D(filters=NUM_FILTER, kernel_size=k, activation='relu',
    kernel_regularizer=regularizers.l2(0.005))(x)
    return GlobalMaxPool1D()(conv) #전체에서 max를 찾기 때문에 Flatten 시킬 필요는 없지만 정보 유실은 있음
    # 시계열 데이터이기 때문에 Conv1D 이용

x_input = Input(batch_shape=(None, x_train.shape[1]))
emb = Embedding(input_dim=VOCAB_SIZE, output_dim=EMB_SIZE)(x_input)
emb = Dropout(rate=0.5)(emb)

h_conv = [conv1d_maxpool(emb, k=i) for i in [3, 4, 5]]
h_concat = Concatenate()(h_conv)
y_output = Dense(1, activation='sigmoid')(h_concat)

model = Model(x_input, y_output)
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0005))
model.summary()

# ======================================================
# 학습
hist = model.fit(x_train, y_train, validation_data = (x_test, y_test), batch_size=1024, epochs=50)

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
y_pred = np.where(pred > 0.5, 1, 0)
accuracy = (y_pred == y_test).mean()
print("\nAccuracy = %.2f %s" % (accuracy * 100, '%'))
# epochs = 30, 50, 100 중에서 50일 때 85.12%로 가장 높게 나왔다.