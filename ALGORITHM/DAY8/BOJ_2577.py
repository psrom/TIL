# 숫자의 개수
import sys

a, b, c = list(int(sys.stdin.readline())for _ in range(3))
calc = list(str(a * b * c))

for i in range(10):
    print(calc.count(str(i)))