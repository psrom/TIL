# 배낭의 가치
# 무게가 적게 나가면서 가치가 높은 것
# 또한 K를 넘지 말아야 함
# n: 물품의 수, k: 버틸 수 있는 최대 무게
n, k = map(int, input().split())

product = [[0, 0]] # 0행 0열 빈 값
a = [[0]*(k+1) for _ in range(n+1)] # (n+1)*(n+1) 2차원 배열

# 물건 무게, 가치 product 행렬에 저장
for _ in range(n):
    product.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = product[i][0] # 무게
        v = product[i][1] # 가치

        if j < w:
            a[i][j] = a[i-1][j]
            print(f'i = {i}, j = {j}, w = {w}')
            for row in a:
                print(row)
        else:
            a[i][j] = max(a[i-1][j], a[i-1][j-w]+v)
            print(f'i = {i}, j = {j}, w = {w}')
            for row in a:
                print(row)

print(a[n][k])


