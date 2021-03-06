# Quora question pairs : CNN 텍스트 유사도 모델
# --------------------------------------------
import numpy as np
from sklearn.model_selection  import train_test_split
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout
from tensorflow.keras.layers import Conv1D, GlobalMaxPool1D, Concatenate
from tensorflow.keras.regularizers import l2
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
import pickle

# --------------------------------------------
DATA_PATH = '/content/drive/MyDrive/DATA/'

# 학습 데이터를 읽어온다.
with open(DATA_PATH + 'qqp.pkl', 'rb') as f:
    q1_data, q2_data, labels, word2idx = pickle.load(f)

# 학습 데이터와 시험 데이터로 나눈다.
q1_train, q1_test, q2_train, q2_test, y_train, y_test = train_test_split(q1_data, q2_data, labels, test_size=0.2)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

# =============================================
# CNN 모델을 빌드한다.
VOCAB_SIZE = len(word2idx)
EMB_SIZE = 16
HIDDEN_SIZE = 32
NUM_FILTER = 32
REG = 0.05

# Question-1, 2 입력용
q1_input = Input(batch_shape=(None, q1_train.shape[1]))
q2_input = Input(batch_shape=(None, q2_train.shape[1]))

# shared embedding
sharedEmb = Embedding(VOCAB_SIZE, EMB_SIZE)

# Question-1 처리용 CNN
q1_emb = sharedEmb(q1_input)
q1_emb = Dropout(rate=0.5)(q1_emb)
q1_conv = Conv1D(NUM_FILTER, 3, activation='relu')(q1_emb)
q1_pool = GlobalMaxPool1D()(q1_conv)
q1_pool = Dense(HIDDEN_SIZE, activation='relu', kernel_regularizer=l2(REG))(q1_pool)
q1_pool = Dropout(rate=0.5)(q1_pool)

# Question-2 처리용 CNN
q2_emb = sharedEmb(q2_input)
q2_emb = Dropout(rate=0.5)(q2_emb)
q2_conv = Conv1D(NUM_FILTER, 3, activation='relu')(q2_emb)
q2_pool = GlobalMaxPool1D()(q2_conv)
q2_pool = Dense(HIDDEN_SIZE, activation='relu', kernel_regularizer=l2(REG))(q2_pool)
q2_pool = Dropout(rate=0.5)(q2_pool)

# Question-1, 2의 출력을 합쳐서 feed forward network으로 마무리 한다.
h_concat = Concatenate()([q1_pool, q2_pool])
outputY = Dense(1, activation='sigmoid')(h_concat)

model = Model([q1_input, q2_input], outputY)
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.0005))
model.summary()

# =============================================
q1_train.shape
# (408072, 31)

# =============================================
# 학습
hist = model.fit([q1_train, q2_train], y_train,
                 validation_data = ([q1_test, q2_test], y_test),
                 batch_size = 4096, epochs = 30)

# =============================================
# Loss history를 그린다
plt.plot(hist.history['loss'], label='Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss history")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# 시험 데이터로 학습 성능을 평가한다
y_prob = model.predict([q1_test, q2_test])
y_pred = np.where(y_prob > 0.5, 1, 0)
accuracy = (y_test == y_pred).mean()
print("Accuracy = %.2f" % (accuracy))
print("log loss = %.4f" % log_loss(y_test, y_prob))

# log loss는 cross entropy를 의미한다.
-(y_test * np.log(y_prob + 1e-8) + (1 - y_test) * np.log(1 - y_prob + 1e-8)).mean()

# Accuracy = 0.78
# log loss = 0.4848
# 0.484845013707922