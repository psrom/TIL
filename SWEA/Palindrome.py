# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문
# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # 행, 열

    letter_lst = []
    result_lst = []
    # 문자 입력 받기
    for i in range(N):
        letter_lst.append(input())

    # 가로 탐색
    for n in range(N):
        for m in range(0, N-M+1):
            if letter_lst[n][m:m+M] == letter_lst[n][m:m+M][::-1]:
                result_lst.append(letter_lst[n][m:m+M])

    # 세로 탐색 => 새로운 배열 만들기(세로 => 가로)
    for m in range(0, N - M + 1):
        for n in range(N):
            c_lst = []
            for i in range(M):
                c_lst.append(letter_lst[m+i][n])
            if c_lst == c_lst[::-1]:
                result_lst.append(''.join(c_lst))

    print(f"#{test_case} {result_lst[0]}")
