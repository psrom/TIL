# Word Embedding & CNN을 이용한 감성분석
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout
from tensorflow.keras.layers import Conv1D, GlobalMaxPool1D, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers
import matplotlib.pyplot as plt
import numpy as np
import pickle

DATA_PATH = '/content/drive/MyDriveDATA/naver_movie/'

# 학습 데이터 불러오기
with open(DATA_PATH + 'naver_movie.pkl', 'rb') as f:
    x_train, x_test, y_train, y_test, word2idx = pickle.load(f)

y_train = np.array(y_train).reshape(-1, 1)
y_test = np.array(y_test).reshape(-1, 1)

# ==================================================
# CNN 모델 생성
VOCAB_SIZE = len(word2idx)
EMB_SIZE = 32
NUM_FILTER = 16

# Convolution & Pooling
def conv1d_maxpool(x, k):
    conv = Conv1D(filters=NUM_FILTER, kernel_size=k,
    activation = 'relu',
    padding='same',
    kernel_regularizer=regularizers.l2(0.01))(x)
    conv = Dropout(rate=0.5)(conv)
    return GlobalMaxPool1D()(conv)

x_input = Input(batch_shape=(None, x_train.shape[1]))
h_emb = Embedding(input_dim=VOCAB_SIZE, output_dim=EMB_SIZE)(x_input)
h_emb = Dropout(rate=0.5)(h_emb)
h_pool = [conv1d_maxpool(h_emb, k=i) for i in [3, 4]]
h_concat= Concatenate()(h_pool)
y_output = Dense(1, activtion = 'sigmoid')(h_concat)

model = Model(x_input, y_output)
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0005))
model.summary()

# ==================================================
# 학습
hist = model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=1024, epochs=50)

# ==================================================
# Loss history
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss history")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 시험 데이터로 학습 성능 평가
pred = model.predict(x_test)
y_pred = np.where(pred > 0.5, 1, 0)
accuracy = (y_pred == y_test).mean()
print("\nAccuracy = %.2f %s" % (accuracy * 100, '%'))