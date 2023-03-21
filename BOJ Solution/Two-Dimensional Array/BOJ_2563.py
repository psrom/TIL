# 색종이 붙이기
n = int(input()) # 색종이 개수

papers = [[0]*100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            papers[x+i][y+j] = 1

result = 0
for i in papers:
    result += sum(i)
print(result)
