# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    bin = format(n, 'b')
    bin = str(bin)
    cnt = bin.count("1")

    for i in range(n + 1, 1000001):
        num = format(i, 'b')
        num_cnt = num.count("1")
        if num_cnt == cnt:
            answer = i
            break
        else:
            continue

    return answer
