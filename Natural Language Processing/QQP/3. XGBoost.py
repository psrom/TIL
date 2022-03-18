# Quora question pairs : XGBoost 텍스트 유사도 모델
import numpy as np
from sklearn.model_selection  import train_test_split
import xgboost as xgb
import pickle
# ===============================================================
DATA_PATH = '/content/drive/MyDrive/DATA/'

# 학습 데이터를 읽어온다.
with open(DATA_PATH + 'qqp.pkl', 'rb') as f:
    q1_data, q2_data, labels, word2idx = pickle.load(f)

# question1과 question2를 하나의 쌍으로 만든다. concatenate.
train_input = np.hstack([q1_data, q2_data])

# 학습 데이터와 시험 데이터로 나눈다.
x_train, x_test, y_train, y_test = train_test_split(train_input, labels, test_size=0.2)
x_train.shape, x_test.shape, y_train.shape, y_test.shape
# ((408072, 62), (102018, 62), (408072,), (102018,))
# x_train[0]

# ===============================================================
# XGBoost로 학습
d_train = xgb.DMatrix(x_train, label=y_train)
d_test = xgb.DMatrix(x_test, label=y_test)
data_list = [(d_train, 'train'), (d_test, 'valid')]

param = {
    'eta': 0.5, 
    'max_depth': 4,  
    'objective': 'binary:logistic',
    'eval_metric': 'logloss'} # eta: 학습율

model = xgb.train(params = param, dtrain = d_train, 
                  num_boost_round = 3000,
                  evals = data_list,
                  early_stopping_rounds=10)

# ===============================================================
# 시험 데이터로 정확도를 계산한다
y_prob = model.predict(d_test)
y_pred = np.where(y_prob > 0.5, 1, 0)
accuracy = (y_test == y_pred).mean()
print("* 정확도 = %.2f" % accuracy)

# log loss = cross entropy
logloss = -(y_test * np.log(y_prob + 1e-8) + 
            (1 - y_test) * np.log(1 - y_prob + 1e-8)).mean()
print("* log loss = %.4f" % logloss)