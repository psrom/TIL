# 평균 조작
# 입력 : 1. 시험 본 과목의 개수 2. 현재 과목별 성적
# 출력 : 새로운 평균
n = int(input())
scores = [int(i) for i in input().split()]

max_score = max(scores)
new_score = [score/max_score * 100 for score in scores]

average = sum(new_score)/n
print(average)