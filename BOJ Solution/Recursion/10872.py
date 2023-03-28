# 재귀로 팩토리얼 풀기
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input())))

