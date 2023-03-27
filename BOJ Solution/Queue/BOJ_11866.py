# 요세푸스 순열
from collections import deque
n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])
ans = [] # 제거 되는 순서

# deque로 구현
while d:
    for i in range(k-1):
        d.append(d.popleft())
    ans.append(d.popleft())

print("<", end="")
for i in range(len(ans)-1):
    print(ans[i], end=", ")
print(ans[-1], end="")
print(">")
