# 완전탐색 알고리즘
# 0~9까지 3개의 숫자가 동일(tripletes) or 3개의 숫자가 연속(run)

num_lst = list(map(int, input().split()))
# print(num_lst)

c = [0] * 10
for num in num_lst:
    c[num] += 1

# print(c)

trip_cnt = 0
run_cnt = 0

i = 0
while i < 10:

    if c[i] >= 3:
        run_cnt += 1
        c[i] -= 3
        
        continue

    i += 1

i = 0
while i < 8:
    if c[i] >= 1 & c[i+1] >= 1 & c[i+2] >= 1:
        trip_cnt += 1
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        
        continue

    i += 1

if run_cnt == 2 or trip_cnt == 2:
    print(True)
elif run_cnt == 1 & trip_cnt == 1:
    print(True)
else:
    print(False)
