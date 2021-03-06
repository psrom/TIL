# Usage examples:
# https://radimrehurek.com/gensim/models/fasttext.html
from gensim.models.fasttext import FastText
import numpy as np

texts = [['human', 'interface', 'computer'],
         ['survey', 'user', 'computer', 'system', 'response', 'time'],
         ['eps', 'user', 'interface', 'system'],
         ['system', 'human', 'system', 'eps'],
         ['user', 'response', 'time'],
         ['trees'],
         ['graph', 'trees'],
         ['graph', 'minors', 'trees'],
         ['graph', 'minors', 'survey']]

# ===============================================================================
model = FastText(size=4, window=3, min_count=1, sentences=texts, 
                 iter=100, bucket=10, min_n=3, max_n=3, sg=0)
# ===============================================================================
# 워드 벡터 확인
model.wv['computer']

# oov라도 다른 벡터를 갖는다
model.wv['comoklksjd']     # 'com' 성분이 포함돼 있다.
model.wv['omplkasjdflkd']  # 'omp' 성분이 포함돼 있다.

# Each word in the vocabulary has an associated vocabulary object, 
# which contains an index and a count
word2idx = {w:obj.index for w, obj in model.wv.vocab.items()}
idx2word = {v:k for k, v in word2idx.items()}

print("사전 크기 =", len(word2idx))
word2idx

# hash table (bucket) 확인. subword들의 워드 벡터가 저장된 공간.
model.wv.vectors_ngrams