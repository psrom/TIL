# 스택 개념
import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    Q = sys.stdin.readline().split()
    order = Q[0]

    if order=="push":
        stack.append(Q[1])

    elif order=="pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)

    elif order=="size":
        print(len(stack))

    elif order=="empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order=="top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
