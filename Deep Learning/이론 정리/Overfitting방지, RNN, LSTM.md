# Overfitting 방지하기

- 복잡한 모델을 단순화하기
- 학습률 조정
- Hidden Layer에서 조정
  - Dropout
  - Regularization
  - BatchNormalization



## BatchNoramalization 

```python
# BatchNoramalization 적용하기
from tensorflow.keras.layers import 

h_1 = Dense(N)(x)
h_2 = BatchNormalization(epsilon = e^(-5))(h_1) #h_1의 출력과 activation 사이에 위치시켜야 한다.
h_3 = Activation("relu")(h_2)
```



### 동작 원리

1. moving average 사용

2. $$
   \gamma, \beta
   $$

​		이 둘은 backpropagation에 의해 학습 대상이 된다. 초기값은 각각 1, 0이다.

3. $$
   \epsilon
   $$

​		분모 = 0을 방지하기 위한 상수를 이용한다.

4.  h_1의 출력(N개)을 표준화 시킨다.

$$
\gamma^i = \frac{h^i - h^i의 이동 평균}{h^i의 이동표준편차 + \epsilon} + \beta^i
$$



| during training                                            | during estimation                                            |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| `model.fit()`                                              | `model.predict()`                                            |
| `delta, beta` 결정. 마지막으로 사용한 평균과 표준편차 이용 | 저장된 `delta, beta, 평균, 표준편차를 이용한다. 이동 평균도 계산하지 않는다. |



## 1. RNN : 순환 신경망

Recurrent Neural Network

| FFN                                                          | RNN                                                          |
| ------------------------------------------------------------ | :----------------------------------------------------------- |
| - data sample 끼리는 영향을 받지 않는다.<br />- 입력 순서와는 무관하다. | - N/W가 이전의 결과를 기억해야 한다.<br />- data sample 2가 입력될 때는 data sample 1을 기억하고 있어야 한다는 뜻이다. |



### RNN 예시

- 시계열 데이터(Time Series)
- 텍스트 데이터(소설, 신문 기사)
- 작곡

위와 같이 순서가 중요한 데이터들이 RNN을 사용하기에 좋다.



### RNN 특징

- 시계열 데이터는 random shuffling 할 수 없다.
- `shape = (b, t, f)` 3차원 구조이다.



### RNN 사용

```python
from tensorflow.keras.layers import Input, Dense, SimpleRnn

xInput = Input(batch_shape = (None, 20, 3))
h = SimpleRNN(2)(xInput)
yOutput = Dense(3)(h)
```



### RNN 이해하기

- 과거의 경험을 바탕으로 미래를 추정한다. 과거와 현재의 관련성을 학습하여 미래를 추정한다. 이 때  `평균`을 이용한다.

$$
a_n = \frac{x_1+x_2+x_3+...+x_n}{n-1} . \frac{n-1}{n}
$$

$$
a_n = a_{n-1}.\frac{n-1}{n} + x_n.\frac{1}{n}
$$

- 2번째 식에서 n-1/n, 1/n은 가중치를 뜻한다. x_n은 새로운 상황이 발생했다는 의미(\\nabla)

$$
a_n = a_{n-1} + \frac{1}{n}.(x_n-a_{n-1})
$$

$$
\frac{1}{n} = \alpha
$$

$$
x_n : 새로운 상황
$$

$$
a_{n-1} : 기존 지식
$$

$$
(x_n-a_{n-1}) : surprise
$$

- surprise 가 발생하면 1/n의 가중치로 a_n이 업데이트 된다. 이를 `학습 과정`이라고 하는 것이다.

- 여기서 \\alpha는 `learning_rate`로 볼 수 있다.

|    alpha가 큰 경우    | alpha가 작은 경우  |
| :-------------------: | :----------------: |
| 새로운 상황 많이 반영 |   기존 지식 우세   |
|      분산이 크다      | 분산이 비교적 작다 |



__우연한 경우 방지하기__

- 학습할 때 <우연한 요소>가 있을 수 있다. 이를 방지하기 위해
  - `Boosting`
  - `K-Fold Cross Validation` 이용



## 2. LSTM

- 기존 RNN의 문제점
  - 장기기억과 단기기억의 영향을 동일하게 취급한다.
  - 작은 gradient가 여러 번 곱해지면 `Gradient Vanishing`이 발생한다. Chain rule에 의해 작은 gradient가 계속 곱해지면 하위단에서는 거의 학습이 일어나지 않는다.

- 이를 보완하기 위해 "Long Term, Short Term Memory" N/W 고안 됨

$$
C_t = f_t \cdot C_{t-1} + N_t \cdot \tilde{C_t}
$$

- `f_t` : forget gate - 기존 지식을 forget하는 정도(가중치)
- `N_t`: input gate = 새로운 경험을 ignore하는 정도(가중치)
- `\tilde{C_t}` : 새로운 경험
- `C_t` : 새로운 지식



:exclamation:__요즘은 주로 LSTM을 이용한다__

\- LSTM보다 조금 더 단순하게 구성된 `GRU`가 사용되기도 한다.
