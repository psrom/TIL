# CountVectorizer, RandomForestClassifier 이용

from numpy import vectorize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle

DATA_PATH = '/content/drive/MyDrive/DATA/movie/'

# 학습 데이터 불러오기
with open(DATA_PATH + 'popcorn.pkl', 'rb') as f:
    x_text, _, y_target, _ = pickle.load(f)

# ======================================================
vectorizer = CountVectorizer(analyzer="word", max_features=5000)
x_feat = vectorizer.fit_transform(x_text)

# ======================================================
# 학습 데이터와 시험 데이터 분리
x_train, x_eval, y_train, y_eval = train_test_split(x_feat, y_target, test_size=0.2)
# x_train.shape, x_eval.shape, y_train.shape, y_eval.shape
# ((20000, 5000), (5000, 5000), (20000,), (5000,))

# ======================================================
forest = RandomForestClassifier(n_estimators=100)
forest.fit(x_train, y_train)

# ======================================================
# 정확도 측정
print('Accuarcy: {:.4f}'.format(forest.score(x_eval, y_eval)))