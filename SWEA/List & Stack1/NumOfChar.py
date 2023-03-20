# 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수
# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    count_dict = {}
    for c in str2:
        if c in count_dict:
            count_dict[c] = count_dict[c] + 1
        else:
            count_dict[c] = 1

    result = []
    for d, value in enumerate(count_dict):
        if value in str1:
            result.append(count_dict[value])
    print(f"#{test_case} {max(result)}")










