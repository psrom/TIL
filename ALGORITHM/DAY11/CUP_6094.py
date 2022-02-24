# 입력: 첫째줄에 번호를 부른 횟수, 두번째 줄에 n개의 랜덤 번호 공백 사이에 두고 입력
# 출력: 출석을 부른 번호 중 가장 빠른 번호 출력
n = int(input())
num = input().split()

for i in range(n):
    num[i] = int(num[i])
min_num = min(num)
print(min_num)