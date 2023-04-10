# LSTM + Conv2D로 mnist 이미지 분석
from tensorflow.keras.layers import Input, Dense, Conv2D, Concatenate, Reshape
from tensorflow.keras.layers import MaxPooling2D, Flatten, LSTM
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# mnist 데이터 코랩에서 불러오기
DATA = '/content/drive/MyDrive/mnist.pkl'
with open(DATA, 'rb') as f:
    mnist = pickle.load(f)

# ==========================================================
x_feat = np.array(mnist.data).reshape(-1, 28, 28) / 255
y_target = np.array(mnist.target.to_numpy().astype('int8')).reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size=0.2)

# ==========================================================
# Convolutional 2D 모델 생성
n_row = x_train.shape[1]
n_col = x_train.shape[2]
n_chan = 1
n_class = len(set(y_train[:, 0]))
n_hidden = 50

x_input = Input(batch_shape=(None, n_row, n_col, n_chan))

# LSTM
h_rnn = LSTM(n_hidden)(x_input)

# CNN
x_input_cnn = Reshape((n_row, n_col, n_chan))(x_input)
h_conv = Conv2D(filters=10, kernel_size=(10, 12), strides=1, padding='valid', activation='relu')(x_input)
h_pool = MaxPooling2D(pool_size=(6, 5), strides=1, padding='valid')(h_conv)
h_flat = Flatten()(h_pool)
h_cnn = Dense(n_hidden, activation='tanh')(h_flat)

# 결합
h_concat = Concatenate()([h_rnn, h_cnn])

y_output = Dense(n_class, activation='softmax')(h_concat)

model = Model(x_input, y_output)
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizers.Adam(learning_rate=0.001))
model.summary()


############################################################
# input을 2개로 나눠서 받을 때 코드
# x1_input = Input(batch_shape=(None, n_row, n_col))
# x2_input = Input(batch_shape=(None, n_row, n_col, 1))
# h_flat = Dense(n_hidden, activation='tanh')(h_flat) # size, 범위 맞추는 용도

# model = Model([x1_input, x2_input], y_output)
# hist = model.fit([x_train, x_train], y_train, batch_size=1024, epochs=50, validation_data=([x_test, x_test], y_test))
###########################################################


# ==========================================================
# 모델 학습
hist = model.fit(x_train, y_train, batch_size=1024, epochs=50, validation_data=(x_test, y_test))


# ==========================================================
# Loss History 그리기
plt.plot(hist.history['loss'], color='blue', label='train')
plt.plot(hist.history['val_loss'], color='red', label='test')
plt.legend()
plt.title("Loss History")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()


# ==========================================================
# 정확도
y_prob = model.predict(x_test)
y_pred = np.argmax(y_prob, axis=1).reshape(-1, 1)
acc = (y_test == y_pred).mean()
print('정확도 = {:.4f}'.format(acc))

df= pd.DataFrame({'y_test': y_test.reshape(-1,), 'y_pred': y_pred.reshape(-1,)})
df.head(10)


# ==========================================================
# 잘못 분류한 이미지 확인
n_sample = 10
miss_cls = np.where(y_test != y_pred)[0]
miss_sam = np.random.choice(miss_cls, n_sample)

fig, ax = plt.subplots(1, n_sample, figsize=(14, 4))
for i, miss in enumerate(miss_sam):
    x = x_test[miss] * 255
    ax[i].imshow(x)
    ax[i].axis('off')
    ax[i].set_title(str(y_test[miss]) + ' / ' + str(y_pred[miss]))