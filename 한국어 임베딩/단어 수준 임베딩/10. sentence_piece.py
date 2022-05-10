# !pip install sentencepiece

# Google의 Sentencepiece 이용
# 챗봇용 학습 문장을 subword token으로 분해
# 코드 구현 : blog.naver.com/chunjein, 2021.03.31
# ===============================================================================
import pandas as pd
import sentencepiece as spm
import re
import pickle

# 챗봇 데이터 파일 읽어오기
%cd '/content/drive/MyDrive/DATA'
corpus = pd.read_csv('ChatBotData.csv', header=0, encoding='utf-8')

#--------------------------------------------------------------------------------
# 질문 + 답변 subword vocabulary 만들기
corpusQA = list(corpus['Q']) + list(corpus['A'])

# 특수문자 제거
corpusQA = [re.sub("([~.,!?\"':;)(])", "", s) for s in corpusQA]
# corpusQA[:10]
# corpus.head()

# Sentence용 사전을 만들기 위해 corpusQA 저장
data_file = "chatbot_data.txt"
with open(data_file, 'w', encoding='utf-8') as f:
    for sent in corpusQA:
        f.write(sent + '\n')

#--------------------------------------------------------------------------------
# Google Sentencepiece를 이용해서 vocabulary 생성
templates= "--input={0:} \
            --pad_id=0 --pad_piece=<PAD>\
            --unk_id=1 --unk_piece=<UNK>\
            --bos_id=2 --bos_piece=<START>\
            --eos_id=3 --eos_piece=<END>\
            --model_prefix={1:} \
            --vocab_size={2:}"

VOCAB_SIZE = 9600
model_prefix = "chatbot_model"
params = templates.format(data_file, model_prefix, VOCAB_SIZE)

spm.SentencePieceTrainer.Train(params)
sp = spm.SentencePieceProcessor()
sp.Load(model_prefix + '.model')

with open(model_prefix + '.vocab', encoding='utf-8') as f:
    vocab = [doc.strip().split('\t') for doc in f]

word2idx = {k:v for v, [k, _] in enumerate(vocab)}
idx2word = {v:k for k, v in word2idx.items()}

# 여기서 수정할 것은 VOCAB_SIZE, model_prefix 이름 정도밖에 없다.
# 이 코드를 이용해서 챗봇을 만든다.

#--------------------------------------------------------------------------------
# string으로 조회
sentence = corpusQA[610]
enc = sp.encode_as_pieces(sentence)
dec = sp.encode.decode_pieces(enc)

print('\n   문장:', sentence)
print('Subwords:', enc)
print('     복원:', dec)
#     문장: 나랑 놀아줘
# Subwords: ['▁나랑', '▁놀아줘']
#     복원: 나랑 놀아줘
#--------------------------------------------------------------------------------
# 수동 decode
print(''.join([x.replace('▁', ' ') for x in enc])[1:])

# word index로 조회
idx = sp.encode_as_ids(sentence)
dec = sp.decode_ids(idx)

print('\n    문장:', sentence)
print('Subwords:', idx)
print('    복원:', dec)
# 나랑 놀아줘

#     문장: 나랑 놀아줘
# Subwords: [1070, 3123]
#     복원: 나랑 놀아줘
#--------------------------------------------------------------------------------
# word index로 변환
corpusQA_idx = [sp.encode_as_idx(qa) for qa in corpusQA]

corpusQA_idx[0]
# [4312, 358, 2447]

corpusQA[0]
# 12시 땡

idx2word[4312]
# ▁12