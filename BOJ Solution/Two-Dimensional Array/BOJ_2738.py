# 행렬 덧셈
n, m = map(int, input().split()) # 행렬의 크기

arr_A = []
arr_B = []

for i in range(n):
    arr_A.append(list(map(int, input().split())))
for i in range(n):
    arr_B.append(list(map(int, input().split())))

ans = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        ans[i][j] = arr_A[i][j] + arr_B[i][j]

for i in range(n):
    print(*ans[i])