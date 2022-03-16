# kaggle <Bag of Words Meets Bags of Popcorn>
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 학습 데이터 읽어오기
DATA_PATH = '/content/drive/MyDrive/DATA/movie'
train_data = pd.read_csv(DATA_PATH+'labeledTrainData.tsv', header=0, sep='\t', quoting=3)
train_data.head()

print('전체 학습 데이터의 개수: {}'.format(len(train_data)))

# ======================================================
# 길이 데이터 추가
train_length = train_data['review'].apply(len)
train_length.head()

# 히스토그램으로 표현
plt.figure(figsize=(12, 5))
plt.hist(train_length, bins=200, alpha=0.5, color='r', lable='word')
# 분포가 치우쳐져 있어서 log처리하여 작은 수로 만들기(음수일 때도 0.0001 같은 값으로 치환)
plt.yscale('log', nonposy='clip') 
plt.title('Log-Histogram of length of review')
plt.xlabel('Length of reivew')
plt.ylabel('Number of review (log scale)')

# 데이터 탐색
print('리뷰 길이 최댓값: {}'.format(np.max(train_length)))
print('리뷰 길이 최솟값: {}'.format(np.min(train_length)))
print('리뷰 길이 평균값: {:.2f}'.format(np.mean(train_length)))
print('리뷰 길이 표준편차: {:.2f}'.format(np.std(train_length)))
print('리뷰 길이 중간값: {}'.format(np.median(train_length)))

# 사분위수는 0~100 사이로 scale 되어있다.
print('리뷰 길이 제1사분위: {}'.format(np.percentile(train_length, 25)))
print('리뷰 길이 제3사분위: {}'.format(np.percentile(train_length, 75)))


# ======================================================
# 시각화

# boxplot
plt.figure(figsize=(12, 5))
plt.boxplot(train_length, labels=['counts'], showmeans=True)
plt.show()

# wordcloud
from wordcloud import WordCloud
cloud = WordCloud(width=800, height=600).genearate(" ".join(train_data['review']))
plt.figure(figsize=(20, 15))
plt.imshow(cloud)
plt.axis('off')

# subplot
fig, axe = plt.subplots(ncols=1)
sns.countplot(train_data['sentiment'])
plt.show()


# ======================================================
# 데이터 탐색

print(train_data['sentiment'].value_counts())
print('\n 긍정 리뷰 개수: {}'.format(train_data['sentiment'].value_counts()[1]))
print('\n 부정 리뷰 개수: {}'.format(train_data['sentiment'].value_counts()[0]))

train_word_counts = train_data['review'].apply(lambda x: len(x.split(' ')))

# 단어 분포 시각화
plt.figure(figsize=(8, 4))
plt.hist(train_word_counts, bins=50, facecolor='r', label='train')
plt.title('Log-Histogram of word count in review')
# plt.yscale('log', noisy='clip')
plt.legend()
plt.xlabel('Number of words')
plt.ylabel('Number of reviews')
plt.ylabel('')

# 단어 데이터 탐색
print('리뷰 단어 개수 최댓값: {}'.format(np.max(train_word_counts)))
print('리뷰 단어 개수 최솟값: {}'.format(np.min(train_word_counts)))
print('리뷰 단어 개수 평균값: {:.2f}'.format(np.mean(train_word_counts)))
print('리뷰 단어 개수 표준편차: {:.2f}'.format(np.std(train_word_counts)))
print('리뷰 단어 개수 중간값: {}'.format(np.median(train_word_counts)))

# 사분위수는 0~100 사이로 scale 되어있다.
print('리뷰 단어 개수 제1사분위: {}'.format(np.percentile(train_word_counts, 25)))
print('리뷰 단어 개수 제3사분위: {}'.format(np.percentile(train_word_counts, 75)))

qmarks = np.mean(train_data['review'].apply(lambda x: '?' in x))
fullstop = np.mean(train_data['review'].apply(lambda x: '.' in x))
capital_first = np.mean(train_data['review'].apply(lambda x: x[0].isupper()))
capitals = np.mean(train_data['review'].apply(lambda x: max([y.isupper() for y in x])))
numbers = np.mean(train_data['review'].apply(lambda x: max([y.isdigit() for y in x])))

print('물음표가 있는 리뷰: {:.2f}'.format(qmarks * 100))
print('마침표가 있는 리뷰: {:.2f}'.format(fullstop * 100))
print('첫 글자가 대문자인 리뷰: {:.2f}'.format(capital_first * 100))
print('대문자가 있는 리뷰: {:.2f}'.format(capitals * 100))
print('숫자가 있는 리뷰: {:.2f}'.format(numbers * 100))