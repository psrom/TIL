# 피보나치 수
n = int(input())
def fib(n):
    if (n==1) or (n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    f = [0]*(n+1)
    f[1], f[2] = 1, 1
    cnt = 0
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        cnt += 1
    return cnt

f = [0 for _ in range(41)]
print(fib(n), fibonacci(n))