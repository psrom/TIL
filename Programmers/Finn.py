# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        result = 0
        while n != result:
            result += i
            i += 1
            if n < result:
                break
            if n == result:
                answer += 1

    return answer
