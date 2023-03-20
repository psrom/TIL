# 소괄호, 대괄호 짝 맞추기
while True:
    s = input()
    if s=='.':
        break
    stack = []
    temp = True

    for br in s:
        if br == '(' or br == "[":
            stack.append(br)
        elif br == ")":
            if not stack or stack[-1]=="[":
                temp = False
                break
            elif stack[-1] == "(":
                stack.pop()
        elif br == "]":
            if not stack or stack[-1] == "(":
                temp = False
                break
            elif stack[-1] == "[":
                stack.pop()
    if temp == True and not stack:
        print("yes")
    else:
        print("no")
