# 입력: 첫째줄에 번호를 부른 횟수
# 두번째 줄에 n개의 랜덤 번호가 공백을 사이에 두고 순서대로 입력
# 출력 : 번호 순서를 바꾸어 공백을 두고 출력
n = int(input())
num = input().split()

for i in range(n):
    num[i] = int(num[i])

for i in range(n-1, -1, -1):
    print(num[i], end= ' ')
