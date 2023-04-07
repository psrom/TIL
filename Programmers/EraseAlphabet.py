# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    lst = [i for i in s]
    stack = []
    for i in range(len(lst)):
        if not stack:
            stack.append(lst[i])
        else:
            p = stack.pop()
            if p == lst[i]:
                continue
            else:
                stack.append(p)
                stack.append(lst[i])
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer