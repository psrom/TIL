# 색종이 붙이기
n = int(input()) # 색종이 개수
w_area = n * 100 # 색종이 크기

# ==========================
papers = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(2):
        # print(papers[i][j])
