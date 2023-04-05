# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = 0

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
