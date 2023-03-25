# 거스름돈 최소 잔돈 개수
A = [500, 100, 50, 10, 5, 1] # 가지고 있는 동전 종류
n = int(input())
m = 1000-n # 거스름 돈

ans = 0
while m != 0:
    for i in range(len(A)):
        l = m // A[i]
        if l > 0:
            ans += l
            m -= A[i]*l
        else:
            pass
print(ans)

