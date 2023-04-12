# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12953
# ====================================================================
# 최소공배수, 최대공약수
# import math
# math.gcd(v1, v2, ...), math.lcm(v1, v2, ..)
# ====================================================================
def solution(arr):
    # 최대공약수 함수
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    answer = arr[0]
    for a in arr:
        answer = answer * a // gcd(answer, a)

    return answer
