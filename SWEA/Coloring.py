# [S/W 문제해결 기본] 2일차 색칠하기

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cnt = 0
    color_board = [[0] * 10 for _ in range(10)]

    # 색칠 영역 입력 받고 list 저장
    coloring = []
    for n in range(N):
        color_interval = list(map(int, input().split()))
        coloring.append(color_interval)

        a1, a2 = coloring[n][0], coloring[n][1]
        b1, b2 = coloring[n][2], coloring[n][3]
        color = coloring[n][4]

        for i in range(a1, b1+1):
            for j in range(a2, b2+1):
                if color == 1:
                    color_board[i][j] += 1
                elif color == 2:
                    color_board[i][j] += 2

                if color_board[i][j] == 3:
                    cnt += 1

    print(f"#{test_case} {cnt}")




