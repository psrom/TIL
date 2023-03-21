# 바구니 뒤집기
# https://www.acmicpc.net/problem/10811
# N: 바구니 개수, M번 바구니 순서 역순
# i, j: i부터 j까지 역순

N, M = map(int, input().split())
basket = [(i+1) for i in range(N)]

for test_case in range(M):
    i, j = map(int, input().split())
    if i-1 == 0:
        basket[i-1:j] = basket[j-1::-1]
    else:
        basket[i-1:j] = basket[j-1:i-2:-1]

print(*basket) # *를 쓰면 원소 출력 가능





