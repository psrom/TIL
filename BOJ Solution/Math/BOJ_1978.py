# 소수 찾기
# 1과 자기 자신을 제외하고는 약수가 없는 수
n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    if num == 1:
        continue
    elif num == 2:
        cnt += 1
        continue
    else:
        cnt_2 = 0
        num_div = [i for i in range(2, num)]
        for d in num_div:
            if num%d == 0:
                break
            else:
                cnt_2 += 1
        if cnt_2 == num-2:
            cnt += 1
print(cnt)