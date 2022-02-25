# 바둑판에 흰 돌 놓기

# 빈 바둑판 만들기
d = [[0 for _ in range(20)] for _ in range(20)]

# 흰 바둑 개수 입력 받고 좌표에 표시
for i in range(int(input())):
    x, y = map(int, input().split())
    d[x][y] = 1

# 바둑판 출력
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end =' ')
    print()




