# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    arr = [0, 1]

    for i in range(2, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])
    answer = arr[n] % 1234567

    return answer