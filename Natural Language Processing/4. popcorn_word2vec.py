# 목적: 입력받은 데이터로 긍정 리뷰인지, 부정 리뷰인지 예측하기
# word2vec 모델 학습을 이용한다.
from sklearn.model_selection import train_test_split
from gensim.models import word2vec
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# 데이터 읽어오기
DATA_PATH = '/content/drive/MyDrive/DATA/movie/'

with open(DATA_PATH + 'popcorn.pkl', 'rb') as f:
    x_text, _, y_target, _ = pickle.load(f)

    word_tok = [word_tokenize(x) for x in x_text]


# ======================================================
# word2vec 모델 생성
num_features = 100
min_word_count = 40 # 40개보다 적으면 버림
context = 10 # 주변 단어 10개
downsampling = 1e-3

model = word2vec.Word2Vecl(word_tok,
sg=1,
negative = 1,
size = num_features,
min_count = min_word_count,
window = context,
sample = downsampling)


# ======================================================
model.wv['stuff']
# 벡터(수치)로 결과 나옴

# ======================================================
# 각 문장의 feature vector 생성
# vector 생성 후 압축 -> 평균내기(수치화)
x_feat = []
for sent in word_tok:
    sent_feat = np.zeros((num_features), dtype=np.float32)

    n = 0
    for word in sent:
        if word in model.wv.index2word:
            sent_feat += model.wv[word]
            n += 1
    x_feat.append(sent_feat / n)
x_feat = np.array(x_feat)
x_feat.shape # (25000, 100)


# ======================================================
# 학습 데이터와 시험 데이터로 분리
x_train, x_eval, y_train, y_eval = train_test_split(x_feat, y_target, test_size=0.2)
# x_train.shape, x_eval.shape, y_train.shape, y_eval.shape
# ((20000, 100), (5000, 100), (20000,), (5000,))

lgs = LogisticRegression(class_weight = 'balanced', max_iter=500)
lgs.fit(x_train, y_train)

print('Accuracy: {:.4f}'.format(lgs.score(x_eval, y_eval)))