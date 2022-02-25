# 입력) 첫 번째 줄에 출석 번호를 부른 횟수인 정수 입력
# 두 번째 줄에 무작위로 부른 n개의 번호(1~23) 공백을 두고 순서대로 입력
# 출력) 1번부터 번호가 불린 횟수를 순서대로 공백 구분하여 한줄로 출력
n = int(input())
num = input().split()

for i in range(n):
    num[i] = int(num[i])

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[num[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')