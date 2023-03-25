# A 배열 수정, B 배열 그대로
# 최솟값 찾기

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 1. 재배열 해서 푸는 경우
# A.sort()
# B.sort()
# B.reverse()
#
# result = 0
# for i in range(n):
#     ans = A[i] * B[i]
#     result += ans
# print(result)

# 2. 재배열 하지 않고 푸는 경우
result = 0
for i in range(n):
    result += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(A.index(min(A)))
print(result)