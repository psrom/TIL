from collections import defaultdict
n, m = map(int, input().split())

hear ={}
see = {}

for _ in range(n):
    hear[input()] = 0
for _ in range(m):
    see[input()] = 0

for s in see:
    if s in hear:
        hear[s] += 1
    else:
        pass

result = []
for key, val in hear.items():
    if val == 1:
        result.append(key)

result.sort()
print(len(result))
for i in result:
    print(i)






