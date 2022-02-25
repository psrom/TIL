# 3의 배수 제외하고 출력
n = int(input())
for i in range(1, n+1):
    if i%3==0:
        continue
    print(i, end=' ')