# 손글씨 데이터 LSTM으로 예측하기
from tensorflow.keras.layers import Input, Dense, LSTM
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# ==========================================================
DATA = '/content/drive/MyDrive/mnist.pkl'
with open(DATA, 'rb') as f:
    mnist =pickle.load(f)

x_feat = np.array(mnist['data']).reshape(-1, 28, 28) / 255
y_target = np.array(mnist['target'].to_numpy().astype('int8')).reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size=0.2)
# x_train.shape, x_test.shape, y_train.shape, y_test.shape

# ==========================================================
# 그래프 모델 생성
n_hNeuron = 50
n_class = len(set(mnist['target']))

xInput = Input(batch_shape=(None, x_train.shape[1], x_train.shape[2]))
hLayer = LSTM(n_hNeuron)(xInput)
yOutput = Dense(n_class,  activation='softmax')(hLayer)

model = Model(xInput, yOutput)
model = compile(loss='sparse_categorical_crossentropy', optimizer='adam')
# model.summary()

# GPU로 실행
hist = model.fit(x_train, y_train, batch_size=1024, epochs=50, validation_data=(x_test, y_test))

# ==========================================================
# error 감소하는 모습 관찰
plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label='Test loss')
plt.legend()
plt.title('Loss function')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# ==========================================================
# 정확도
y_prob = model.predict(x_test)
y_pred = np.argmax(y_prob, axis=1).reshape(-1,1)
acc = (y_test == y_pred).mean()
print('정확도 ={:.4f}'.format(acc))

# 정답과 추정값 표로 보기
df = pd.DataFrame({'y_test': y_test.reshape(-1,), 'y_pred': y_pred.reshape(-1,)})
df.head()

# ==========================================================
# 잘못 분류한 이미지 확인
n_sample = 10
miss_cls = np.where(y_test != y_pred)[0]
miss_sam = np.random.choice(miss_cls, n_sample)

fig, ax = plt.subplots(1, n_sample, figsize=(14, 4))
for i, miss in enumerate(miss_sam):
    x = x_test[miss] * 255 # 표준화 값에서 원래의 값으로 변환
    ax[i].imshow(x)
    ax[i].axis('off')
    ax[i].set_title(str(y_test[miss] + ' / ' + str(y_pred[miss])))