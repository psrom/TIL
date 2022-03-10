from tensorflow.keras.layers import Dense, Input, SimpleRNN
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2차원 배열의 feature 데이터로 LSTM 학습 데이터 만들기
def build_train_data(data, t_step, n_jump = 1):
    n_data = data.shape[0]
    n_feat = data.shape[1]

    m = np.arange(0, n_data - t_step, n_jump)
    x = np.array([data[i:(i+t_step), :] for i in m])
    y = np.array([data[i, :] for i in (m + t_step)])

    # shape 조정
    x_data = x.reshape(-1, t_step, n_feat)
    y_target = y.reshape(-1, n_feat)

    return x_data, y_target

# ==========================================================
# 시계열 데이터 (noisy sin)
n_data = 1000
sine = np.sin(2 * np.pi * 0.03 * np.arange(n_data) + np.random.random(n_data))

# 데이터프레임 형식으로 변환
df = pd.DataFrame({'sine': sine})
# df.head() 데이터 프레임 확인

t_step = 20

# 학습 데이터 생성
data = np.array(df)
x_train, y_train = build_train_data(data, t_step)
# x_train.shape, y_train.shape

n_input = 1 # feature
n_output = 1 # value
n_hidden = 50 # hidden layer

# RNN 모델 생성
xInput = Input(batch_shape = (None, t_step, n_input)) # (size, time, feature)
x_lstm = SimpleRNN(n_hidden)(xInput)
yOutput = Dense(n_output)(x_lstm)

model = Model(xInput, yOutput)
model.compile(loss="mean_squared_error", optimizer=Adam(lr=0.001))
# model.summary(line_length=120)

# 모델 학습
h = model.fit(x_train, y_train, epochs = 20, batch_size = 100, shuffle = True)

# ==========================================================
# Loss history 그리기
plt.figure(figsize=(8, 3))
plt.plot(h.history['loss'], color = 'red')
plt.title("Loss History")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# ==========================================================
# 향후 20 기간 데이터 예측. 향후 1 기간을 예측하고, 예측값을 다시 입력하여 2기간을 예측한다.
# 이 방법으로 20 기간까지 예측.
n_future = 20
n_last = 100 # plot 확인용
last_data = data[-n_last:]

for i in range(n_future):
    # 마지막 t_step 만큼 입력 데이터로 다음 값을 예측
    px = last_data[-t_step:, :].reshape(1, t_step, 1) # 3차원인 것 주의

    # 다음 값 예측
    y_hat = model.predict(px)

    # 이전 예측값을 포함하여 다음 값을 예측하기 위해 예측값 저장하기
    last_data = np.vstack([last_data, y_hat])

past_data = last_data[:n_future, :]
future_data = last_data[-(n_future + 1):, :]

# last_data.shape, past_data.shape, future_data.shape


# ==========================================================
# 기존 시계열과 예측된 시계열 그리기
plt.figure(figsize=(12, 6))
ax1 = np.arange(1, len(past_data) + 1)
ax2 = np.arange(len(past_data), len(past_data) + len(future_data))
plt.plot(ax1, past_data, 'b-o', color = 'blue', markersize=3, label="Time Series", linewidth = 1)
plt.plot(ax2, future_data, 'b-o', color = 'red', markersize=3, label="Estimated")
plt.axvline(x=ax1[-1], linestyle='dashed', linewidth=1)
plt.legend()
plt.show()

# ==========================================================
# 점간 사이 거리가 먼 경우 예측의 정도가 떨어지는 게 일반적