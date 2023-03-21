# 최댓값과 위치 찾기
# 9*9 행렬 0 <= N <= 99

arr = [list(map(int, input().split())) for i in range(9)]

max_lst = []
max_rc = []

for i in range(9):
    max_lst.append(max(arr[i]))
    ans = max(max_lst)
    max_rc = [[i+1, j+1] for i in range(9) for j in range(9) if arr[i][j] == ans]

print(max(max_lst))
for i in max_rc:
    print(*i)
