# 영미문학 소설 SkipGram모델 만들기
# colaboratory와 jupyter notebook 사전 개수 차이 있음(이유: 모름. 텐서플로우 버전 차이일 것으로 추정)

# 공공 GPU에서 실행시 한 명이 먼저 점유하면 나머지는 사용을 못해서
# 다른 사람들은 아래 코드 입력해서 CPU로 돌려야 함
# GPU를 찾지 않겠다는 코드(tensorflow는 기본적으로 GPU를 사용함)
# import os
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"

from pickletools import optimize
import numpy as np
import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from nltk.stem import LancasterStemmer
from tensorflow.keras.layers import Input, Embedding, Dense
from tensorflow.keras.models import Model
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('gutenberg')
nltk.download('stopwords')

# ===============================================================================
# 영문 소설 18개를 읽어와서 전처리 수행
n = 18
stemmer = LancasterStemmer()
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(['and', 'but', 'the', 'for', 'would', 'shall'])

sent_stem = []
files = nltk.corpus.gutenberg.fileids()
for i, text_id in enumerate(files[:n]):
    text = nltk.corpus.gutenberg.raw(text_id)
    sentences = nltk.sent_tokenize(text)

    # 각 단어에 Lancaster stemmer 적용
    for sentence in sentences:
        word_tok = nltk.word_tokeinze(sentence)
        stem = [stemmer.stem(word) for word in word_tok if word not in stopwords if len(word)>2]
        sent_stem.append(stem)
    print('{}: {} -------- processed.'.format(i+1, text_id))

print("\n총 문장 개수=", len(sent_stem))
print(sent_stem[0]) # 첫번째 문장 출력

# ===============================================================================
# 단어사전 만들기
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sent_stem)

# 단어사전
word2idx = tokenizer.word_index
word2idx['<PAD>'] = 0
idx2word = {v:k for k, v in word2idx.items()}

print("사전 크기 =", len(word2idx))

# ===============================================================================
# 문장을 단어의 인덱스로 표현
sent_idx = tokenizer.texts_to_sequences(sent_stem)
print(sent_idx[0])

# ===============================================================================
# trigram
x_train = []
y_train = []
for sent in sent_idx:
    if len(sent) < 3:
        continue
    
    for a, b, c in nltk.trigrams(sent):
        x_train.append(b)
        x_train.append(b)

        y_train.append(a)
        y_train.append(c)

x_train = np.array(x_train).reshape(-1,1)
y_train = np.array(y_train).reshape(-1,1)

# ===============================================================================
VOC_SIZE = len(word2idx)
EMB_SIZE = 32

x_input = Input(batch_shape=(None, 1))
x_emb = Embedding(VOC_SIZE, EMB_SIZE, name='emb')(x_input)
y_output = Dense(VOC_SIZE, activation='softmax')(x_emb)

model = Model(x_input, y_output)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.summary()

# word --> word2vec을 확인하기 위한 모델(중간 출력 확인)
model_vec = Model(x_input, x_emb)

# ===============================================================================
# 학습
hist = model.fit(x_train, y_train, batch_size=20480, epochs=1)

# ===============================================================================
def get_word2vec(word):
    stem_word = stemmer.stem(word)
    if stem_word not in word2idx:
        print('{}가 없습니다.'.format(word))
        return
    
    word2vec = model_vec.predict(np.array(word2idx[stem_word]).reshape(1,1))[0]
    return word2vec

# ===============================================================================
father = get_word2vec('father')
mother = get_word2vec('mother')
doctor = get_word2vec('doctor')

print(father)

# ===============================================================================
cosine_similarity(father, mother)
cosine_similarity(father, doctor)

# ===============================================================================
W = model.get_layer('emb').get_weights()[0]
W.shape
# (32545, 32)

# 계산량이 너무 많다.