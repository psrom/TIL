from collections import deque
import sys

n, m = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))

dq = deque(list([k for k in range(1, n+1)]))
cnt = 0

for num in nums:
    while True:
        if dq[0] == num:
            dq.popleft()
            break

        else:
            if dq.index(num) < len(dq)/2:
                while dq[0] != num:
                    d2 = dq.popleft()
                    dq.append(d2)
                    cnt += 1

            else:
                while dq[0] != num:
                    d2 = dq.pop()
                    dq.appendleft(d2)
                    cnt += 1

print(cnt)

