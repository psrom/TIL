# 제로
# ==============================
# 0을 입력 받으면 가장 최근 수를 지움
# 스택으로 구현
# ==============================

import sys
k = int(sys.stdin.readline())
stack = []

for i in range(k):
    number = int(sys.stdin.readline())
    if number !=0 :
        stack.append(number)
    elif number == 0:
        stack.pop()

print(sum(stack))
