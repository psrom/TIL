n, m = map(int, input().split())
board = list([input() for i in range(n)])
result = []

for i in range(n-7):
    for j in range(m-7):
        w_idx, b_idx = 0, 0
        for a in range(i, i+8): # 8행
            for b in range(j, j+8): # 8열
                if (a+b) % 2 == 0:
                    if board[a][b] != "W": # W로 시작했는데 짝수번째가 W가 아닌 경우
                        w_idx += 1
                    else:
                        b_idx += 1
                else:
                    if board[a][b] != "W": # B로 시작했는데 홀수번째가 W가 아닌 경우
                        b_idx += 1
                    else:
                        w_idx += 1
        result.append(w_idx)
        result.append(b_idx)

print(min(result))