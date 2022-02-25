# numbers = [i for i in range(5)]
# even_numbers = [i for i in range(0, 10, 2)]

n, m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(board)