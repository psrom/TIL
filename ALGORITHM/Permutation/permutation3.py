# 1, 2, 3, 4 순열 만들기
num_lst = [1, 2, 3, 4]
n = 0
# ============================================================================
# 1
# for i, val1 in enumerate(num_lst):
#     for j, val2 in enumerate(num_lst):
#         if val1 != val2:
#             for k, val3 in enumerate(num_lst):
#                 if (val1 != val3) & (val2 != val3):
#                     for l, val4 in enumerate(num_lst):
#                         if (val1 != val4) & (val2 != val4) & (val3 != val4):
#                             n += 1
#                             print([val1, val2, val3, val4], f" #", n)
# ============================================================================
# 2

l = len(num_lst)
for i in range(l):
    for j in range(l):
        if i != j:
            for k in range(l):
                if (i != k) & (j != k):
                    for m in range(l):
                        if (i != m) & (j != m) & (k != m):
                            n += 1
                            print([num_lst[i], num_lst[j], num_lst[k], num_lst[m]], f" #", n)
