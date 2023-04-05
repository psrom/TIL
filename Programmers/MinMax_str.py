def solution(s):
    s = s.split(" ")
    lst = []
    for i in range(len(s)):
        lst.append(int(s[i]))

    mx = max(lst)
    mn = min(lst)

    answer = f"{mn} {mx}"
    return answer