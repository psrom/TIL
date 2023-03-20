# 델타를 이용한 2차 List 탐색
# arr[0 ... n-1][0 ... n-1]: 2차원 list
n = 100
arr = [[0] for i in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(arr[testX][testY])

# ==========================================
# 전치 행렬
# i: 행의 좌표, len(arr)
# j: 열의 좌표, len(arr[0])
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# ===========================================
# zip 함수
alpha = ["a", "b", "c"]
index = [1, 2, 3]
alpha_index = list(zip(alpha, index))
print(alpha_index)

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(zip(*arr)))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]