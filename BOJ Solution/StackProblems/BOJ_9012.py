# 괄호 문제
for _ in range(int(input())):
    s = input()

    vps = True
    stack = []
    for c in s:
        if c=="(":
            stack.append(c)
        elif c==")":
            if not stack:
                vps = False
                break

            stack.pop()

    if stack:
        vps = False

    print("Yes" if vps else "No")