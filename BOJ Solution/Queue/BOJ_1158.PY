def solution(s):
    s = s.split(" ")
    lst = list(s)

    for a in range(len(lst)):
        if (type(lst[a][0])) != str:
            lst[a] = lst[a][0] + lst[a][1:].lower()
        else:
            lst[a] = lst[a][0].upper() + lst[a][1:].lower()

    answer = " ".join(lst)
    return "\""+answer+"\""
solution("for the last week")
