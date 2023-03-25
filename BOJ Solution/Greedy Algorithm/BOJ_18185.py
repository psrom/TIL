# 1개 공장 = 3원
# 2개 공장 = 5원
# 3개 공장 = 7원

n = int(input()) # 라면 공장 개수
r_arr = list(map(int, input().split())) # 공장에서 살 라면 개수
ans = 0

for i in range(n-2):
    # 2번째가 3번째보다 값이 큰 경우
    # ex) 1 2 1 1
    # 이 경우 1 1 구매 후 0 1 1 1 구매하는 것이 이득
    if r_arr[i+1] > r_arr[i+2]:
        m = min(r_arr[i], r_arr[i+1]-r_arr[i+2])
        ans += m*5
        r_arr[i] -= m
        r_arr[i+1] -= m

    if (r_arr[i] > 0) and (r_arr[i+1] > 0) and (r_arr[i+2] > 0):
        m = min(r_arr[i], r_arr[i+1])
        ans += m*7
        r_arr[i] -= m
        r_arr[i+1] -= m
        r_arr[i+2] -= m

    if r_arr[i] > 0:
        ans += r_arr[i] * 3

# for문으로 돌릴 수 없는 범위
if (r_arr[-2] > 0) and (r_arr[-1] > 0):
    m = min(r_arr[-2], r_arr[-1])
    ans += m*5
    r_arr[-2] -= m
    r_arr[-1] -= m

if r_arr[-2] > 0:
    ans += (r_arr[-2]*3)
else:
    ans += (r_arr[-1] * 3)

print(ans)








