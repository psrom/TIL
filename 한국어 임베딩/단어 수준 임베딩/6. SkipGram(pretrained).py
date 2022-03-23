# Google's pre-trained Word2Vec 사용 예시
# download : https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit
# ---------------------------------------------------------------------------
import gensim
import numpy as np

# Load Google's pre-trained Word2Vec model.
path = 'd:/GoogleWord2Vec/GoogleNews-vectors-negative300.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(path, binary=True)

# 오류 나서 나중에 질문할 것