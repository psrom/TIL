# word2vec 방식으로 SkipGram 모델 생성
import numpy as np
import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from nltk.stem import LancasterStemmer
from gensim.models import word2vec
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('gutenberg')
nltk.download('stopwords')

# ===============================================================================
# 영문 소설 18개를 읽어와서 전처리를 수행한다.
n = 18
stemmer = LancasterStemmer()
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(['and', 'but', 'the', 'for', 'would', 'shall'])

sent_stem = []
files = nltk.corpus.gutenberg.fileids()
for i, text_id in enumerate(files[:n]):
    text = nltk.corpus.gutenberg.raw(text_id)
    sentences = nltk.sent_tokenize(text)

    # 각 단어에 Lancaster stemmer를 적용한다.
    for sentence in sentences:
        word_tok = nltk.word_tokenize(sentence)
        stem = [stemmer.stem(word) for word in word_tok if word not in stopwords if len(word) > 2]
        sent_stem.append(stem)
    print('{}: {} ----- processed.'.format(i+1, text_id))

print("\n총 문장 개수 =", len(sent_stem))
print(sent_stem[0])

# ===============================================================================
# 모델 생성
model = word2vec.Word2Vec(sent_stem, size =32, window=1, sg=1, negative=1)

# ===============================================================================
# Each word in the vocabulary has an associated vocabulary object,
# which contains an index and a count
word2idx = {w:obj.index for w, obj in model.wv.vocab.items()}
idx2word = {v:k for k, v in word2idx.items()}

print("사전 크기=", len(word2idx))

# ===============================================================================
def stem(word):
    stem_word = stemmer.stem(word)
    if stem_word not in word2idx:
        print('{}가 없습니다.'.format(word))
        return '_'
    else:
        return stem_word

def get_word2vec(word):
    stem_word = stem(word)
    if stem_word == '_':
        return
    
    word2vec = model.wv[stem_word]
    return word2vec

def most_similar(word):
    stem_word = stem(word)
    if stem_word == '_':
        return
    
    return model.wv.most_similar(stem_word)

def similarity(w1, w2):
    stem_w1 = stem(w1)
    stem_w2 = stem(w2)
    if stem_w1 == '_' or stem_w2 == '_':
        return

    return model.wv.similarity(stem_w1, stem_w2)
# ===============================================================================
# get_word2vec('father')
# similarity('father', 'mother')
# similarity('father', 'doctor')

# queen1 = get_word2vec('queen').reshape(1, -1)
# queen2 = (get_word2vec('king') - get_word2vec('man') + get_word2vec('woman')).reshape(1, -1)
# cosine_similarity(queen1, queen2)

# similarity('dog', 'cat')
# similarity('dog', 'car')