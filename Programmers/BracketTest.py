def solution(s):
    answer = True
    lst = []
    for i in s:
        lst.append(i)
    que = []

    for i in range(len(lst)):
        if lst[i] == "(":
            que.append("(")
        else:
            if que:
                que.pop()
            else:
                answer = False
    if que:
        answer = False

    return answer