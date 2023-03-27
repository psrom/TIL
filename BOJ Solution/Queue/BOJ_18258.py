from collections import deque
import sys
# sys 안 넣으면 시간 초과 됨

n = int(input())
dq = deque([])

for i in range(n):
    o = sys.stdin.readline().split()
    if o[0] == "push":
        dq.appendleft(o[1])

    elif o[0] == "pop":
        if dq:
            print(dq.pop())
        else:
            print(-1)

    elif o[0] == "size":
        if dq:
            print(len(dq))
        else:
            print(0)

    elif o[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)

    elif o[0] == "front":
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)

    elif o[0] == "back":
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
