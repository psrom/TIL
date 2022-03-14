# CNN

Convolutional Neural Network 합성곱 신경망

- 시계열 데이터 분석
- 이미지 분석



## [0] 데이터 구조

- **순환 신경망 many_to_one** : CNN이 사용하는 구조

  - x_train : 3차원, t축(time step) 존재

  - feature는 여러 개, y_train은 1개의 feature만 학습

- 순환 신경망 many_to_many
  - x_train : 3차원, t축 존재
  - y_train : x축 갯수만큼 feature 학습

---

## [1] Conv 1D

- FFN 네트워크 사용
- t축의 **sequence**를 분석한다.
- 입력 : 3D 구조



#### >> 과정

1. filter가 있는 안경으로 데이터를 관찰한다.

   t축을 따라 안경이 내려간다. :arrow_right: **stride** : 이동하는 칸 수

2. 관찰할 때마다 특징을 요약해서 숫자로 정리한다.

   :arrow_right: 이 과정을 **Convolutional**이라고 한다.

   :arrow_right: 특징을 정리해둔 곳은 **Feature Map**

3. 다른 filter의 안경으로 위를 반복한다.

4. **Grid**로 max 값을 저장한다. // **pooling**이라고 한다.(optional)
5. 일렬로 나열한다.
6. y_train의 결과를 하나로 출력한다.



#### **>> filter**

- CNN에서는 filter가 학습 대상(trainable parameter)이다.
- 처음: random :arrow_right:원소들을 통해 update(Gradient Decent 이용)
- :star:filter를 통해 이미지의 부분적인 특징을 추출해낸다.

---

**padding** : feature map의 크기 조절용. data feature의 경계

row data feature와 feature map의 크기를 동일하게 해줌



### 코드

```python
from tensorflow.keras.layers import Input, Dense, Conv1D, MaxPooling1D, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers
from sklearn.model_selection import train_test_split

x_feat = np.array(mnist['data']).reshape(-1, 28, 28) / 255
y_tarteg = np.array(mnist['target'].to_numpy().astype('int8')).reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size=0.2)
>>> x_train.shape, x_test.shape, y_train.shape, y_test.shape
((56000, 28, 28), (14000, 28, 28), (56000, 1), (14000, 1))

# =============================================
# Conv1D 모델 생성
n_row = x_train.shape[1]
n_col = x_train.shape[2]
n_class = len(set(y_train[:, 0])) # 10 종류

x_input = Input(batch_shape=(None, n_row, n_col))
h_conv = Conv1D(filters=30, kernel_size=6, strides=1, padding='same', activation='relu')
h_pool = MaxPooling1D(pool_size=4, strides=1, padding='valid')(h_conv)
h_flat = Flatten()(h_pool)
y_output = Dense(n_class, activation='softmax')(h_flat)

model = Model(x_input, y_output)
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizers.Adam(ls=0.001))
```



## [2] Conv 2D

spatial convolution

- 컬러 이미지 분석용(rgb)
- 4D 구조
  - 이미지 1개는 3D구조, 이를 channel축(R, G, B)로 두기 때문에 4D



### 코드

```python
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers
from sklearn.model_selection import train_test_split

x_feat = np.array(mnist['data']).reshape(-1, 28, 28, 1) / 255
y_tarteg = np.array(mnist['target'].to_numpy().astype('int8')).reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x_feat, y_target, test_size=0.2)
>>> x_train.shape, x_test.shape, y_train.shape, y_test.shape
((56000, 28, 28, 1), (14000, 28, 28, 1), (56000, 1), (14000, 1))

# =============================================
# Conv1D 모델 생성
n_row = x_train.shape[1]
n_col = x_train.shape[2]
n_class = len(set(y_train[:, 0])) # 10 종류

x_input = Input(batch_shape=(None, n_row, n_col, 1))
h_conv = Conv2D(filters=10, kernel_size=(10, 12), strides=(1, 1), padding='same', activation='relu')
h_pool = MaxPooling2D(pool_size=4, strides=1, padding='valid')(h_conv)
h_flat = Flatten()(h_pool)
y_output = Dense(n_class, activation='softmax')(h_flat)

model = Model(x_input, y_output)
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizers.Adam(ls=0.001))
```

