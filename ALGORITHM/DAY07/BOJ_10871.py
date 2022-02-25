# x 보다 작은 수
import sys
n, x = map(int,sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
for number in numbers:
    if number < x:
        print(number, end=' ')