# A Neural Probabilistic Language Model (NPLM)
#
# NPLM 논문 : Yoshua Bengio, et. al., 2003, A Neural Probabilistic Language Model
# 코드 구현 : blog.naver.com/chunjein, 2021.03.22
# -------------------------------------------------------------------------------
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Input, Embedding, Dense, Add, Flatten, LSTM
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

# ===============================================================================
data = ["The cat is walking in the bedroom",
        "A dog was running in a room",
        "The cat is running in a room",
        "A dog is walking in a bedroom",
        "The dog was walking in the room"]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(data)
word2idx = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(data) # 사전을 인덱스로 표시

# ===============================================================================
import nltk
x, y = [], []
for sent in sequences:
  for a, b, c, d in nltk.ngrams(sent, 4):
    x.append([a, b, c])
    y.append(d)
x = np.array(x)
y = np.array(y)
x.shape, y.shape
# ((20, 3), (20,))

# ===============================================================================
# -------------------------------------------------------------------------------
# x[:5]
# array([[ 1,  8,  4],
#        [ 8,  4,  5],
#        [ 4,  5,  2],
#        [ 5,  2,  1],
#        [ 3,  6, 10]])

# y[:5]
# array([ 5,  2,  1,  9, 11])
# -------------------------------------------------------------------------------
# ===============================================================================
def prepare_sentence(seq, maxlen):
    # Pads seq and slides windows
    x = []
    y = []
    for i, w in enumerate(seq[1:], 1):
        x.append(pad_sequences([seq[:i]], maxlen=maxlen - 1)[0])
        y.append(w)
    return x, y
# ===============================================================================
# 학습 데이터를 생성한다.
maxlen = 4
x = []
y = []
for seq in sequences:
    x_, y_ = prepare_sentence(seq, maxlen)
    x += x_
    y += y_
    
x_train = np.array(x)
y_train = np.array(y)

x_train.shape, y_train.shape
# ((30, 3), (30, ))
# ===============================================================================
# -------------------------------------------------------------------------------
# x_train[:10]
# array([[ 0,  0,  1],
#        [ 0,  1,  8],
#        [ 1,  8,  4],
#        [ 8,  4,  5],
#        [ 4,  5,  2],
#        [ 5,  2,  1],
#        [ 0,  0,  3],
#        [ 0,  3,  6],
#        [ 3,  6, 10],
#        [ 6, 10, 11]], dtype=int32)
# -------------------------------------------------------------------------------
# 이후 코드는 1.NPLM과 같다.