# a, b 입력 받고 a+b 출력
import sys
try:
    while True:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
except ValueError:
    pass

# 처음에 런타임 에러(ValueError) 떠서 try, except 추가