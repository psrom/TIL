# .capitalize()
# .capwords(): capitalize + split + join

# 1. capitalize() 이용
def solution(s):
    s = s.split(" ")
    temp = []
    for i in s:
        i = i.capitalize()
        temp.append(i)
    return " ".join(temp)

# 2. capwords() 이용
import string
def solution2(s):
    return string.capwords(s, sep = " ")