#주사위 세개 같은 눈의 수에 따라 상금 받기
a, b, c = map(int, input().split())

if a==b and b==c:
    total = 10000 + a * 1000
    print(total)
elif a==b and a!=c:
    total = 1000 + a * 100
    print(total)
elif b==c and a!=b:
    total = 1000 + b * 100
    print(total)
elif c==a and a!=b:
    total = 1000 + c * 100
    print(total)
else:
    total = max(a, b, c) * 100
    print(total)