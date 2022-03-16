from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

DATA_PATH = '/content/drive/MyDrive/DATA/movie/'

# 학습 데이터 읽어오기
with open(DATA_PATH + 'popcorn.pkl', 'rb') as f:
    x_text, _, y_target, _ = pickle.load(f)

vectorizer = TfidfVectorizer(min_df=0.0, analyzer="char", subliner_tf=True, ngram_range=(1, 3), max_teatures=5000)
x_feat = vectorizer.fit_transform(x_text)


# ======================================================
# 학습 데이터와 시험 데이터로 분리
x_train, x_eval, y_train, y_eval = train_test_split(x_feat, y_target, test_size=0.2)
x_train.shape, x_eval.shape, y_train.shape, y_eval.shape
# ((20000, 5000), (5000, 5000), (20000,), (5000,))


# ======================================================
# target 개수가 imbalanced 할 때
lgs = LogisticRegression(class_weight = 'balanced')
lgs.fit(x_train, y_train)

# 영화 리뷰 데이터 감성 분석 정확도
print('Accuracy: {:.4f}'.format(lgs.score(x_eval, y_eval)))