from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd

# Google colab에서 실행
DATA = '/content/drive/MyDrive/mnist.pkl'
with open(DATA, 'rb') as f:
    mnist = pickle.load(f)

x_feat = np.array(mnist.data).reshape(-1, 28, 28, 1) / 255 # 28 * 28 배열 3차원
y_target = np.array(mnist.target.to_numpy().astype('int8')).reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size=0.2)
# x_train.shape, x_test.shape, y_train.shape, y_test.shape

# ==========================================================
# Convolutional 1D 모델 생성
n_row = x_train.shape[1]
n_col = x_train.shape[2]
n_chan = x_train.shape[3]
n_class = len(set(y_train[:, 0])) # 0, 1, ..., 9 총 10개의 category

x_input = Input(batch_shape = (None, n_row, n_col, n_chan))
h_conv = Conv2D(filters=10, kernel_size=(10, 12), strides=1, padding='same', activation='relu')
h_pool = MaxPooling2D(pool_size=4, strides=1, padding='valid')(h_conv)
h_flat = Flatten()(h_pool)
y_output = Dense(n_class, activation='softmax')(h_flat)

model = Model(x_input, y_output)
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizers.Adam(lerning_rate=0.001))
model.summary(line_length=80)


# ==========================================================
# 모델 학습
hist = model.fit(x_train, y_train, batch_size=1024, epochs=50, validation_data=(x_test, y_test))


# ==========================================================
# Loss History 그리기
plt.plot(hist.history['loss'], color='blue', label='train')
plt.plot(hist.history['val_loss'], color='red', label='test')
plt.legend()
plt.title("Loss History")
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()


# ==========================================================
# 정확도 측정
y_prob = model.predict(x_test)
y_pred = np.argmax(y_prob, axis=1).reshape(-1, 1)
acc = (y_test==y_pred).mean()
print('정확도 ={:.4f}'.format(acc))


# ==========================================================
df = pd.DataFrmae({'y_test': y_test.reshape(-1,), 'y_pred': y_pred.reshape(-1,)})
df.head(10)


# ==========================================================
# 잘못 분류한 이미지의 갯수와 해당 이미지 확인
n_sample = 10
miss_cls = np.where(y_test != y_pred)[0]
miss_sam = np.random.choice(miss_cls, n_sample)

fig, ax = plt.subplots(1, n_sample, figsize=(14,4))
for i, miss in enumerate(miss_sam):
    x = np.squeeze(x_test[miss], axis=-1) * 255
    ax[i].imshow(x)
    ax[i].axis('off')
    ax[i].set_title(str(y_test[miss]) + ' / ' + str(y_pred[miss]))