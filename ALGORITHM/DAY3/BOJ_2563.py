# 도화지를 만든다.
paper = [[0] * 100 for _ in range(100)]

# 색종이 칠하기
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

# 영역의 넓이 출력 (도화지에서 1인 부분 다 더하기)
total = 0
for i in range(100):
    for j in range(100):
        total += paper[i][j]
print(total)

# total = sum(sum(line) for line in paper)