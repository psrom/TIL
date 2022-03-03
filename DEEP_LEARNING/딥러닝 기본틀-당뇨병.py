# 당뇨병 진단 딥러닝
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split

import pandas as pd
DATA_PATH = '/content/drive/MyDrive/DATA/'
diabetes = pd.read_csv(DATA_PATH + 'diabetes.csv')

diabetes.head()

x_feat = diabetes.iloc[:, :-1]
y_target = diabetes['Outcome'].to_numpy().reshape(-1, 1)
print(x_feat.shape, y_target.shape)

# 표준화
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_feat)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_target, test_size=0.2)
x_train.shape, y_train.shape

# 네트워크 생성
xInput = Input(batch_shape=(None, x_train.shape[1]), name = 'In')
hidden = Dense(10, activation = "relu")(xInput)
yOutput = Dense(y_train.shape[1], activation = 'sigmoid', name = 'Out')(hidden)

model = Model(xInput, yOutput)
model.compile(loss="binary_crossentropy", optimizer="adam")

model.summary()

hist = model.fit(x_train, y_train, batch_size=50, epochs=300, validation_data=(x_test, y_test))

# error 시각화
import matplotlib.pyplot as plt
plt.plot(hist.history['loss'], label = 'Train loss')
plt.plot(hist.history['val_loss'], label = 'Test loss')
plt.legend()
plt.title("Loss function")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

y_prob = model.predict(x_test)
y_pred = (y_prob>0.5).astype('int8')

acc = (y_test == y_pred).mean()
print(acc)

