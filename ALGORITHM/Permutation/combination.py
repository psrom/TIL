# 123 조합 만들기

num_lst = [1, 2, 3]
n = 0

# =========================================
# 1
# for i, val1 in enumerate(num_lst):
#     for j, val2 in enumerate(num_lst):
#         for k, val3 in enumerate(num_lst):
#             n += 1
#             print([val1, val2, val3])
# =========================================
# 2
l = len(num_lst)
for i in range(l):
    for j in range(l):
        for k in range(l):
            n += 1
            print([num_lst[i], num_lst[j], num_lst[k]])
print("총 " + str(n) + "개")
