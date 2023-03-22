# 이분탐색으로 풀기
# n개로 이루어진 정수
# 정수 위치 찾기

n = int(input())
set = list(map(int, input().split()))

def binary_search(find_num):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end) // 2
        if find_num == set[mid]:
            return mid
        elif find_num > set[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(binary_search(int(input())))