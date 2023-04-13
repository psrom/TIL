# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    if n == 1:
        return 1 % 1234567
    elif n == 2:
        return 2 % 1234567
    else:
        arr = [1, 2]
        result = 0
        for i in range(2, n):
            arr.append(arr[i - 2] + arr[i - 1])

        return arr[-1] % 1234567
