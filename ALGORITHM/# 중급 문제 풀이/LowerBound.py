n = int(input())
nums = list(map(int, input().split()))

# nums[k-1] < target & nums[k] >= target인 k찾기
def LowerBound(k):
    s = 0
    e = len(nums)

    while s < e:
        m = (s+e)//2
        if nums[m] < k:
            s = m+1
        else:
            e = m
    return s+1

print(LowerBound(int(input())))