nums = list(map(int, input().split()))

while nums != [1, 2, 3, 4, 5]:
    for i in range(4):
        if nums[i] > nums[i+1]:
            tmp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = tmp
            print(*nums)