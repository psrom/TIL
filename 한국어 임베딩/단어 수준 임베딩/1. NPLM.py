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
# sequences 뒤에 <EOS> 추가
word2idx_len = len(word2idx)
word2idx['<PAD>'] = 0
word2idx['<EOS>'] = word2idx_len + 1 # end of sentence 추가
idx2word = {v: k for (k, v) in word2idx.items()}
sequences = [s + [word2idx['<EOS>']] for s in sequences]

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
# 학습 데이터 생성
maxlen = max([len(s) for s in sequences])
x = []
y = []
for seq in sequences:
    x_, y_ = prepare_sentence(seq, maxlen)
    x += x_
    y += y_

x_train = np.array(x)
y_train = np.array(y)

x_train.shape, y_train.shape
# ((35, 7), (35,))

# -----------------------------------------------------------
# x_train[:10]
# array([[ 0,  0,  0,  0,  0,  0,  1],
#        [ 0,  0,  0,  0,  0,  1,  8],
#        [ 0,  0,  0,  0,  1,  8,  4],
#        [ 0,  0,  0,  1,  8,  4,  5],
#        [ 0,  0,  1,  8,  4,  5,  2],
#        [ 0,  1,  8,  4,  5,  2,  1],
#        [ 1,  8,  4,  5,  2,  1,  9],
#        [ 0,  0,  0,  0,  0,  0,  3],
#        [ 0,  0,  0,  0,  0,  3,  6],
#        [ 0,  0,  0,  0,  3,  6, 10]], dtype=int32)

# y_train[:10]
# array([ 8,  4,  5,  2,  1,  9, 12,  6, 10, 11])
# -----------------------------------------------------------
# ===============================================================================
# NPLM 모델 생성
EMB_SIZE = 8
VOCAB_SIZE = len(word2idx)
x_input = Input(batch_shape = (None, x_train.shape[1]))
x_embed = Embedding(input_dim = VOCAB_SIZE, output_dim=EMB_SIZE, name='emb')

# H-network
h_layer = Dense(10, activation='tanh')(x_embed)

# U-network
u_layer = Dense(10)(h_layer)

# W-network
w_layer = Dense(10)(x_embed)

# 전체 네트워크
t_layer = Add()([u_layer, w_layer])
t_layer = Flatten()(t_layer)
y_output = Dense(VOCAB_SIZE, activation='softmax')(t_layer)

model = Model(x_input, y_output)
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizers.Adam(learning_rate=0.01))
model.summary()

# ===============================================================================
# 모델 학습
hist = model.fit(x_train, y_train, epochs=300, verbose=0) # 과정 안 뜨게 하는 코드 `verbose=0`

# ===============================================================================
# Loss history를 그린다
plt.plot(hist.history['loss'], label='Train loss')
plt.legend()
plt.title("Loss history")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

# ===============================================================================
C = model.get_layer('emb').get_weights()[0]
C.shape
# (13, 8)

# ===============================================================================
# 한 단어의 워드 벡터를 조회한다.
word = 'dog'
w_idx = word2idx[word]
wv = C[w_idx, :]  # look-up
print('\n단어 :', word)
print('인덱스 :', w_idx)
print(np.round(wv, 3))
# -----------------------------------------------------------
# 단어 : dog
# 인덱스 : 6
# [-0.04   0.362 -0.008 -0.235 -0.292 -0.326 -0.111 -0.309]
# -----------------------------------------------------------
# ===============================================================================
def get_prediction(model, sent):
    x = tokenizer.texts_to_sequences(sent)[0]
    x = pad_sequences([x], maxlen=maxlen - 1)[0]
    x = np.array(x).reshape(1, -1)
    return model.predict(x)[0]

# 주어진 문장 다음에 나올 단어를 예측한다.
x_test = ['A dog is walking in a']
p = get_prediction(model, x_test)
n = np.argmax(p)
prob = p[n]
next_word = idx2word[n]
print("\n{} --> '{}', probability = {:.2f}%".format(x_test, next_word, prob * 100))
