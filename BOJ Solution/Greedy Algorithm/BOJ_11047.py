# N종류의 동전
# 합 K
# 필요 동전 최소 개수

# 첫째줄에 N, K
# 둘째 줄부터 동전 가치 오름차순 정렬
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

use_coins = []
for c in coins:
    if c > K:
        pass
    else:
        use_coins.append(c) # K보다 작은 코인들 사용

cnt = 0
use_coins = reversed(use_coins)

while K != 0:
    for u in use_coins:
        q = K // u
        if q > 0:
            cnt += q
            K -= u*q
        else:
            pass
print(cnt)





