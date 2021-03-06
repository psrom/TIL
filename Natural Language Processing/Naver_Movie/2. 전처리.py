# 네이버 영화 후기 감성분석을 위한 전처리
# !pip install konlpy
import pandas as pd
import numpy as np
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import re
import pickle
from tqdm.auto import tqdm
DATA_PATH = '/content/drive/MyDrive/DATA'

train_data = pd.read_csv(DATA_PATH + 'naver_movie/ratings_train.txt', sep='\t')
test_data = pd.read_csv(DATA_PATH + 'naver_movie/ratings_test.txt', sep='\t')
train_data = train_data.dropna()
test_data = test_data.dropna()
# train_data.head()

# ==================================================
# 전처리 작업
stop_words = ['은', '는', '이', '가', '하', '아', '것', '들', '의', '있', '되', '수', '보', '주', '등', '한']
okt = Okt()
clean_train = []

def preprocessing(review, okt, remove_stopwords = False, stop_words = []):
    review_text = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s","", review) # 한글을 제외한 문자들 공백으로 치환
    word_review = okt.morphs(review_text, stem=True)

    if remove_stopwords:
        word_review = [token for token in word_review if not token in stop_words]

    return word_review

def cleaning(df):
    clean_data = []
    for i, review in tqdm(enumerate(df['document']), total = len(df['docment'])):
        # 비어있는 데이터에서 멈추지 않도록 string인 경우만 진행
        if type(review) == str:
            p = preprocessing(review, okt, remove_stopwords=True, stop_words=stop_words)
            clean_data.append(p)
        else:
            clean_data.append([]) #string이 아니면 빈 값 추가
            print(i, review)

    return clean_data

# ==================================================
clean_train = cleaning(train_data)
clean_test = cleaning(test_data)

# ==================================================
# 전체 vocab size = 43,756 이중 빈도수 상위 20000개만 사용
VOCAB_SIZE=20000
tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token='<OOV>')
tokenizer.fit_on_texts(clean_train) # train 데이터로만 사전 생성

# 각 단어를 사전의 index로 표현
train_seq = tokenizer.texts_to_sequences(clean_train)
test_seq = tokenizer.texts_to_sequences(clean_test)

# 20000개 단어 사전 생성
word2idx = {k:v for k, v in tokenizer.word_index.items() if v < VOCAB_SIZE}
word2idx['<PAD>'] = 0

MAX_SEQ_LEN = 8 # 문장 최대 길이
x_train = pad_sequences(train_seq, maxlen=MAX_SEQ_LEN, padding='post', truncating='post')
x_test = pad_sequences(test_seq, maxlen=MAX_SEQ_LEN, padding='post', truncating='post')

y_train = np.array(train_data['label'])
y_test = np.array(test_data['label'])

# ==================================================
# 학습 데이터 저장
with open(DATA_PATH + 'naver_movie/naver_movie.pkl', 'wb') as f:
    pickle.dump([x_train,x_test,y_train,y_test,word2idx], f, pickle.DEFAULT_PROTOCOL)