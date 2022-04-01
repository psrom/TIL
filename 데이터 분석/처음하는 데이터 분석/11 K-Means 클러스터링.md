# 비지도 학습: K-Means 클러스터링

- 고객 세분화, 상권 세분화와 같은 답이 없는 형태

- 유사성의 기준: `거리`이므로 `수치형` 변수가 필요하다.
  - 물리적인 거리
  - 추상적인 거리: 둘은 유사한 사람인가? 어떤 사람과 더 비슷한가?



## Normalization

```python
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

weather = pd.read_csv('data/weather.csv')
X = np.array(weather.humidity).reshape(-1, 1)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_scaled
```

## K-Means 클러스터링

- 시간대 별로 대여 횟수가 비슷한 구끼리 구분하기

```python
n_bike = pd.pivot_table(bike_data2, index=['Gu', 'Date_out', 'Time_out'], values='Distance', aggfunc=len)
n_bike = n_bike.reset_index()
n_bike.rename(columns={'Distance':'Count'}, inplace=True)
n_bike
#----------------------------------------
# pivot_table로 다시 압축(3일치의 평균)
n_bike2 = pd.pivot_table(n_bike, index='Gu', columns='Time_out', values='Count', aggfunc=np.mean)
n_bike2 = n_bike2.reset_index()
n_bike2
#----------------------------------------
# 군집 나누기
from sklearn import cluster

X = n_bike2.iloc[0:5, 1:25]
y = n_bike2.Gu
km2 = cluster.KMeans(n_clusters=2).fit(X)
km3 = cluster.KMeans(n_clusters=3).fit(X)
km4 = cluster.KMeans(n_clusters=4).fit(X)
#----------------------------------------
# 군집 결과 확인하기
n_bike2['2_Cluster'] = km2.labels_
n_bike2['3_Cluster'] = km3.labels_
n_bike2['4_Cluster'] = km4.labels_
n_bike2[['Gu', '2_Cluster', '3_Cluster', '4_Cluster']]
```

- 군집화할 대상이 많은 경우 `K-Means` 유용하다.



