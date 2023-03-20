# for loop 으로 permutation 만들기

num_lst = [1, 2, 3]

# ========================================================
# 1
# n = 0
# for i, val1 in enumerate(num_lst):
#     for j, val2 in enumerate(num_lst):
#         if val1 != val2:
#             for k, val3 in enumerate(num_lst):
#                 if (val1 != val3) & (val2 != val3):
#                     n += 1
#                     print([val1, val2, val3], f" #", n)

# ========================================================
# 2
# n = 0
#
# for i, val1 in enumerate(num_lst):
#     for j, val2 in enumerate(num_lst):
#         if i != j :
#             for k, val3 in enumerate(num_lst):
#                 if (i != k) & (j != k):
#                     n += 1
#                     print([val1, val2, val3], f" #", n)
# ========================================================
# 3

cnt = 0
l = len(num_lst)

for i in range(l):
    for j in range(l):
        if i != j:
            for k in range(l):
                if (i != k) & (j != k):
                    cnt += 1
                    print([num_lst[i], num_lst[j], num_lst[k]], f" #", cnt)
