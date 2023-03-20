# 완전탐색 알고리즘
# 0~9까지 3개의 숫자가 동일(tripletes) or 3개의 숫자가 연속(run)

num_lst = list(map(int, input().split()))
print(num_lst)

run_cnt = 0
tripl_cnt = 0

for i in range(len(num_lst)):
    for j in range(len(num_lst)):
        if i != j:
            

# print(run_cnt, tripl_cnt)