# 공 넣기
# 바구니 N개, 방법 M줄
# i, j, k는 i~j 바구니까지 k번 번호가 적힌 공 넣기
# 바구니에 들어있는 공 번호 출력

N, M = map(int, input().split())
arr = [0 for _ in range(0, N+1)]

for test_case in range(1, 1+M):
    i, j, k = map(int, input().split())

    for n in range(i, j+1):
        arr[n] = k

for n in arr[1::]:
    print(n, end = " ")