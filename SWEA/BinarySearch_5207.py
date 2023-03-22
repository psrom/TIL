# 5207 이진탐색
# r, l 몇 번 왔다 갔다 하는지
T = int(input())
N, M = map(int, input().split())
arr = list(map(int, input().split()))
case = list(map(int, input().split()))

def count_rl():
    start = 0
    end = N-1

