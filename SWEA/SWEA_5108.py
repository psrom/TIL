# 숫자 추가

for test_case in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        i, v = map(int, input().split())
        arr.insert(i, v)
    print(f'#{test_case} {arr[L]}')

