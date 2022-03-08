# google colaboratory에서 실행
# 자전거를 몇 대 대여하는지 예측하는 프로그램(kaggle 데이터 이용)

# 필요한 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l1, l2, l1_l2

# 데이터 불러오기
DATA_PATH = '/content/drive/MyDrive/DATA/bike'
data = pd.read_csv(DATA_PATH + 'train.csv')

# ==========================================================
# 전처리 과정
# datetime열에서는 연/월/시간 중 '시간'만 이용한다.
data['datetime'] = pd.to_datetime(data['datetime'])
data['hour'] = data['datetime'].apply(lambda x : x.hour)

# count = casual + registered 이므로 count열만 이용
# temp와 atemp 둘 다 온도에 관한 데이터이므로 temp만 이용
# one-hot encoding 필요한 열 : season, weather, hour
x = data.drop['casual', 'regisered', 'atemp', 'datetime']
x = pd.get_dummies(x, columns = ['season', 'weather', 'hour'])

scaler = StandardScaler()
temp_s = scaler.fit_transform(x['temp'].values.reshape(-1, 1))
hum_s = scaler.fit_transform(x['humidity'].values.reshape(-1, 1))
wind_s = scaler.fit_transform(x['windspeed'].values.reshape(-1, 1))
count_s = scaler.fit_transform(x['count'].values.reshape(-1, 1))

x['temp'] = temp_s
x['humidity'] = hum_s
x['windspeed'] = wind_s
x['count'] = count_s

y = x.pop('count')
y = np.array(y).reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# ==========================================================
# 딥러닝 네트워크 구성

xInput = Input(batch_shape = (None, x_train.shape[1]))
hLayer = Dense(10, activation = 'relu')(xInput)
for i in range(4):
    hLayer = Dense(10, activation='relu')(hLayer)
yOutput = Dense(y_train.shape[1])(hLayer)

model = Model(xInput, yOutput)
model = compile(loss = 'mean_squared_error', optimizer = Adam(lr = 0.001))

# ==========================================================
# 학습
hist = model.fit(x_train, y_train, batch_size=50, epochs=100, validation_data = (x_test, y_test))

# ==========================================================
# r2값 출력

y_pred = model.predict(x_test)
R2 = r2_score(y_test, y_pred)
print(R2)

# ==========================================================
# error 감소하는 plot 관찰

plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()


# 개선해야 할 점
# humidity, windspeed 중 0인 값들을 처리해주어야 함