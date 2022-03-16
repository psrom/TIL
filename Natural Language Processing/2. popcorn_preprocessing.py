import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import nltk
import re
from nltk.stem import PoterStemmer
import pickle
import numpy as np

nltk.download('punkt')
nltk.download('stopwords')

# ======================================================
# 학습 데이터 읽어오기
DATA_PATH = '/content/drive/MyDrive/DATA/movie'

train_data = pd.read_csv(DATA_PATH + 'labeledTrainData.tsv', header=0, sep='\t', quoting=3)
# train_data['review'][0]

# ======================================================
# Pre-processing
stemmer = PoterStemmer()
stopwords = nltk.corpus.stopwords.words('english')

clean_text = []
for review in train_data['review']:
    # 1. 영문자와 숫자만 사용(이외 문자는 공백 문자로 대체)
    review = review.replace('<br />', ' ')
    review = review.replace('\'', ' ')
    review = re.sub("[^a-zA-Z]", ' ', review)

    tmp = []
    for word in nltk.word_tokenize(review):
        # 2. 불용어 처리
        # e.g는 e g로 처리된 상태. 한글자 word는 버린다
        if len(word.lower()) > 1 and word.lower() not in stopwords:
            # 3. Stemming
            tmp.append(stemmer.stem(word.lower()))
    clean_text.append(' '.join(tmp))

# clean_text[0]


# ======================================================
# tokenize
tokenizer = Tokenizer()
tokenizer.fit_on_texts(clean_text)
text_sequences = tokenizer.texts_to_sequences(clean_text)

# print(text_sequences[0])


# ======================================================
# 사전 제작
word2idx = tokenizer.word_index
word2idx['<PAD>'] = 0
print(word2idx)
print("전체 단어 개수:", len(word2idx))

# {'movi': 1, 'film': 2, 'one': 3, 'like': 4, 'time': 5, 'good': 6, 'make': 7, 'charact': 8, 'get': 9, 'see': 10, 'watch': 11, 'stori': 12, 'even': 13, 'would': 14, 'realli': 15, 'well': 16, 'scene': 17, 'look': 18, 'show': 19, 'much': 20, 'end': 21, 'peopl': 22, 'bad': 23, 'go': 24, 'great': 25, 'also': 26, 'first': 27, 'love': 28
# 전체 단어 개수: 50102


# ======================================================
MAX_SEQ_LENGTH = 174 # 한 문장 최대 길이
train_inputs = pad_sequences(text_sequences, maxlen=MAX_SEQ_LENGTH, padding='post')
print('Shape of train data: ', train_inputs.shape)

train_labels = np.array(train_data['sentiment'])
print('Shape of label tensor: ', train_labels.shape)

# Shape of train data:  (25000, 174)
# Shape of label tensor:  (25000,)


# ======================================================
# 학습 데이터 저장하기
with open(DATA_PATH + 'popcorn.pkl', 'wb') as f:
    pickle.dump([clean_text, train_inputs, train_labels, word2idx], f, pickle.DEFAULT_PROTOCOL)