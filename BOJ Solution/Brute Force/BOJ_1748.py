# 수 이어 쓰기
n = input()
l = len(n)-1
c = 0
i = 0

while i < l:
    c += 9 * (10**i) * (i+1)
    i += 1
c += ((int(n) - (10**l)) +1) * (l + 1)
print(c)
