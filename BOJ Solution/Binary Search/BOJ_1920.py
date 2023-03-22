# 정수 존재하는지 알아보기
# 1. 이진 분류 사용 X
# n = int(input())
# A = set(map(int, input().split()))
#
# m = int(input())
# M = list(map(int, input().split()))
#
# for i in M:
#     print(1) if i in A else print(0)


# 2. 이진 분류 사용 O
n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
M = list(map(int, input().split()))

for k in M:
    start = 0
    end = n - 1
    isExist = False
    while start <= end:
        mid = (start + end) // 2
        if k == A[mid]:
            isExist = True
            print(1)
            break
        elif k > A[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if not isExist:
        print(0)