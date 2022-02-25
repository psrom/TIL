# 빛 섞어 색 만들기
r, g, b = map(int, input().split())
colors = [r, g, b]

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
print(r*g*b)