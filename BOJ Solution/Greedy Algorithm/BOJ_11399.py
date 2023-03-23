# ATM 시간 합 최소
n = int(input())
time = list(map(int, input().split()))
time = sorted(time)

whole_time = 0
# 총 걸리는 시간 찾기
for i, v in enumerate(time):
    whole_time += v * (n-i)
print(whole_time)