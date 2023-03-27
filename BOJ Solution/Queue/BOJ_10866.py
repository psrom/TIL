# 덱 구현
import sys
from collections import deque
n = int(input())
dq = deque([])

for i in range(n):
    o = sys.stdin.readline().split()
    if o[0] == "push_front":
        dq.appendleft(o[1])

    elif o[0] == "push_back":
        dq.append(o[1])

    elif o[0] == "pop_front":
        if dq:
            d = dq.popleft()
            print(d)
        else:
            print(-1)

    elif o[0] == "pop_back":
        if dq:
            d = dq.pop()
            print(d)
        else:
            print(-1)

    elif o[0] == "size":
        if dq:
            print(len(dq))
        else:
            print(0)

    elif o[0] == "empty":
        if not dq:
            print(1)
        else:
            print(0)

    elif o[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)

    elif o[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
