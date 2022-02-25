board = [list(input()) for _ in range(8)]
white = 0

for i in range(8):
    for j in range(8):
        if i % 2 == j % 2 and board[i][j] == "F": #세로로 찾을 때는 [j][i]
            white += 1
print(white)

# print(sum(input()[i % 2 ::2].count("F") for i in range(8)))