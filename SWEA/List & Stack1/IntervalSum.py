# [S/W 문제해결 기본] 1일차 구간합

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    # N: 정수의 개수
    # M: 구간의 개수
    num_lst = list(map(int, input().split()))  # 정수 입력 받기
    sum_lst = []

    for i in range(N-M+1):
        result = 0
        for j in range(i, i+M):
            result += num_lst[j]
        sum_lst.append(result)
    print(f"#{test_case} {max(sum_lst)-min(sum_lst)}")















