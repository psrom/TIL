# 3의 배수는 x로 출력
# input = 7
# output = 1 2 X 3 4 5 X 7

n = int(input())
for i in range(1, n+1):
    if i % 3 == 0: # n/3*3 == n으로 작성 가능
        print("X", end=" ")
    else:
        print(i, end=" ")
