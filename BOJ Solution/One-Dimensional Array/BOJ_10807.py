# 총 N개의 정수가 주어졌을 때,
# 정수 v가 몇 개인지 구하는 프로그램

N = int(input()) # N개의 정수
num_list = list(map(int, input().split()))
V = int(input())

count_num = 0
for n in num_list:
    if n == V:
        count_num += 1
    else:
        continue

print(count_num)




