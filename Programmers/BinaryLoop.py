# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt = 0
    cnt_0 = 0

    while s != "1":
        cnt_0 += s.count("0")
        s = s.replace("0", "")
        l = len(s)
        l = format(l, 'b')
        s = l
        cnt += 1
        answer = [cnt, cnt_0]

    return answer
