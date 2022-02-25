# 바둑알 십자 뒤집기

# 입력 받을 바둑판
d = [list(map(int, input().split())) for _ in range(19)]

# 십자 뒤집기 횟수와 좌표 입력
# 0->1, 1->0
for i in range(int(input())):
    x, y = map(int, input().split())
    for j in range(19):
        if d[x-1][j] == 0:
            d[x-1][j] = 1
        else:
            d[x-1][j]=0

        if d[j][y-1] == 0:
            d[j][y-1] = 1
        else:
            d[j][y-1]=0

# 십자 뒤집기 한 바둑판 출력
for i in range(19):
    for j in range(19):
        print(d[i][j], end = ' ')
    print()