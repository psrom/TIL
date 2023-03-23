n = int(input())
nums = list(map(int, input().split()))
k = int(input()) #찾고자 하는 값

def UpperBound(k):
    s = 0
    e = len(nums)

    while s < e:
        m = (s+e)//2
        if nums[m] <= k:
            s = m + 1
        else:
            e = m
    return s+1

print(UpperBound(k))