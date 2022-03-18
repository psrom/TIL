import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

DATA_PATH = '/content/drive/MyDrive/DATA/naver_movie/'

train_data = pd.read_csv(DATA_PATH + 'ratings_train.txt', header=0, delimiter='\t', quoting=3)
train_data.head()

print('전체 학습 데이터의 개수: {}'.format(len(train_data)))

# ==================================================
# 리뷰 길이 관찰
train_length = train_data['document'].astype(str).apply(len)
train_length.head()

plt.figure(figsize=(12, 5))
plt.hist(train_length, bins=200, alpha=0.5, color = 'r', label='word')
plt.yscale('log', nonposy='clip')
plt.title('Log Histogram of length of review')
plt.xlabel('Length of review')
plt.ylabel('Number of review')

print('리뷰 길이 최댓값: {}'.format(np.max(train_length)))
print('리뷰 길이 최솟값: {}'.format(np.min(train_length)))
print('리뷰 길이 평균값: {:.2f}'.format(np.mean(train_length)))
print('리뷰 길이 표준편차: {:.2f}'.format(np.std(train_length)))
print('리뷰 길이 중간값: {}'.format(np.median(train_length)))
print('리뷰 길이 제1사분위: {}'.format(np.percentile(train_length, 25)))
print('리뷰 길이 제3사분위: {}'.format(np.percentile(train_length, 75)))

# ==================================================
# box plot
plt.boxplot(train_length,
            labels=['counts'],
            showmeans=True)

# ==================================================
# 워드 클라우드를 한글 데이터로 생성하면 깨진다.
# 아래 코드를 실행하려면 해당 폴더에 ttf 파일이 있어야 함
train_review = [review for review in train_data['document'] if type(review) is str]

wordcloud = WordCloud(font_path = DATA_PATH + 'NanumGothic.ttf').generate(' '.join(train_review))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# ==================================================
# 긍정, 부정 갯수 관찰
fig, axe = plt.subplots(ncols=1)
fig.set_size_inches(6, 3)
sns.countplot(train_data['label'])

print("긍정 리뷰 개수: {}".format(train_data['label'].value_counts()[1]))
print("부정 리뷰 개수: {}".format(train_data['label'].value_counts()[0]))

# ==================================================
# 리뷰에 쓰인 단어 갯수 확인
train_word_counts = train_data['document'].astype(str).apply(lambda x:len(x.split(' ')))
plt.figure(figsize=(15, 10))
plt.hist(train_word_counts, bins=50, facecolor='r', label='train')
plt.title('Log-Histogram of word count in review', fontsize=15)
plt.yscale('log', nonposy='clip')
plt.legend()
plt.xlabel('Number of words', fontsize=15)
plt.ylabel('Number of reviews', fontsize=15)

print('리뷰 단어 최댓값: {}'.format(np.max(train_word_counts)))
print('리뷰 단어 최솟값: {}'.format(np.min(train_word_counts)))
print('리뷰 단어 평균값: {:.2f}'.format(np.mean(train_word_counts)))
print('리뷰 단어 표준편차: {:.2f}'.format(np.std(train_word_counts)))
print('리뷰 단어 중간값: {}'.format(np.median(train_word_counts)))
print('리뷰 단어 제1사분위: {}'.format(np.percentile(train_word_counts, 25)))
print('리뷰 단어  제3사분위: {}'.format(np.percentile(train_word_counts, 75)))

# ==================================================
# 느낌표, 마침표가 있는 질문 비율
qmarks = np.mean(train_data['document'].astype(str).apply(lambda x: '?' in x))
fullstop = np.mean(train_data['document'].astype(str).apply(lambda x: '.' in x))

print('물음표가 있는 질문: {:.2f}%'.format(qmarks*100))
print('마침표가 있는 질문: {:.2f}%'.format(fullstop*100))