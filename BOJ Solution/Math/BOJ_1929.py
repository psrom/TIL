# m과 n 사이의 소수
m, n = map(int, input().split())
prime_num = []
for i in range(m, n+1):
    condition = True
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            condition = False
            break
    if condition:
        prime_num.append(i)

print(*prime_num, sep='\n')
