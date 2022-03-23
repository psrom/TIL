# 영미문학 소설 SGNS모델 만들기
# Skip Gram Negative Sampling
import numpy as np
import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from nltk.stem import LancasterStemmer
from tensorflow.keras.layers import Input, Embedding, Dense, Dot, Activation, Flatten
from tensorflow.keras.models import Model
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.utils import shuffle

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
# 학습 데이터 생성
# trigram
x_train_t = [] # target word
x_train_c = [] # context word

# positive data
for sent in sent_idx:
    if len(sent) < 3:
        continue

    for a, b, c in nltk.trigrams(sent):
        x_train_t.append(b)
        x_train_t.append(b)
        x_train_c.append(a)
        x_train_c.append(c)
    y_train_pos = [1] * len(x_train_t)

# negatve sampling. random이 오래 걸려서 아래처럼 일괄처리
ns_k = 1 # 데이터가 클 때는 2~5배, 작을 때는 5~20배 해주면 된다.
x_train_nt = [] # negative target word
x_train_nc = [] # negative context word
for k in range(ns_k):
    r = np.random.choice(range(1, len(word2idx)), len(x_train_t))
    x_train_nt.extend(x_train_t.copy())
    x_train_nc.extend(list(r).copy())
y_train_neg = [0] * len(x_train_t) * ns_k

# positive + negative
x_target = x_train_t + x_train_nt
x_context = x_train_c + x_train_nc
y_train = y_train_pos + y_train_neg

# shuffling
x_target, x_context, y_train = shuffle(x_target, x_context, y_train)

# list --> array 변환
x_target = np.array(x_target).reshape(-1, 1)
x_context = np.array(x_context).reshape(-1, 1)
y_train = np.array(y_train).reshape(-1, 1)

x_target.shape, x_context.shape, y_train.shape

# ===============================================================================
VOC_SIZE = len(word2idx)
EMB_SIZE = 32

x_input_t = Input(batch_shape=(None, 1))
x_input_c = Input(batch_shape=(None, 1))

SharedEmb = Embedding(VOC_SIZE, EMB_SIZE, name = 'emb')
x_emb_t= SharedEmb(x_input_t)
x_emb_c = SharedEmb(x_input_c)

y_output = Dot(axes=(2, 2))([x_emb_t, x_emb_c])
y_output = Activation('sigmoid')(y_output)

model = Model([x_input_t, x_input_c], y_output)
model.compile(loss='binary_crossentropy', optimizer='adam')
model.summary()

# word --> word2vec을 확인하기 위한 모델
model_vec = Model(x_input_t, x_emb_t)

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