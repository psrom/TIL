# Quora question pairs
import pandas as pd
import numpy as np
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Quora question 데이터 읽어오기
DATA_PATH = '/content/drive/MyDrive/DATA/'
df = pd.read_csv(DATA_PATH + 'quora_question_pairs.csv')
df.head()

# ===============================================================
# 중복된 페어와 중복되지 않은 페어로 분리
pos_data = df.loc[df['is_duplicate']==1]
neg_data = df.loc[df['is_duplicate']==1]

# 중복되지 않은 페어가 많으므로 둘의 비율이 비슷하도록 조절
# sample_frac(%) 만큼 샘플링
f = len(neg_data) / len(pos_data)
print("before: %.2f" % f)

# 이 경우 f > 1
sample_data = pos_data.sample(frac = f - 1, replace=True) # up sampling
f = len(neg_data) / (len(pos_data) + len(sample_data))
print("after: %.2f" % f)

# ===============================================================
# 데이터를 다시 합친다.
df = pd.concat([neg_data, pos_data, sample_data])

# FILTERS에 포함된 문자 제거
# 소문자 변환
q1 = [str(s) for s in df['question1']]
q2 = [str(s) for s in df['question2']]

q1_filt = [re.sub("([~.,!?\"':;)(])", " ", q).lower() for q in q1]
q2_filt = [re.sub("([~.,!?\"':;)(])", " ", q).lower() for q in q2]

# ===============================================================
# 사전을 구축하고 단어를 워드 인덱스로 변환
# 전체 76,610 단어 중 상위 빈도 50,000개만 사용
VOCAB_SIZE = 50000
tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token='<OOV>')
tokenizer.fit_on_texts(q1_filt + q2_filt)

# 각 단어를 사전의 인덱스로 표시
q1_seq = tokenizer.texts_to_sequences(q1_filt)
q2_seq = tokenizer.texts_to_sequences(q2_filt)

# 50,000개 짜리 사전 생성
word2idx = {k:v for k, v in tokenizer.word_index.items() if v < VOCAB_SIZE}
word2idx['<PAD>'] = 0

# ===============================================================
# 한 문장의 길이를 31개로 제한
MAX_SEQ_LEN = 31
q1_data = pad_sequences(q1_seq, maxlen=MAX_SEQ_LEN, padding='post', truncating='post')
q2_data = pad_sequences(q2_seq, maxlen=MAX_SEQ_LEN, padding='post', truncating='post')
labels = np.array(df['is_duplicae'], dtype=int)

# ===============================================================
# 전처리 결과 저장해두기
with open(DATA_PATH + "qqp.pkl", "wb") as f:
    pickle.dump([q1_data, q2_data, labels, word2idx], f, pickle.DEFAULT_PROTOCOL)

# q1_data.shape
# (510090, 31)///