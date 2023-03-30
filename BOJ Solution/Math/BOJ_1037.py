# 진짜 약수를 이용해서 N 구하기
n = int(input())
lst = list(map(int, input().split()))

min_lst = min(lst)
max_lst = max(lst)

if min_lst == 1:
    print(max_lst**2)
else:
    print(max_lst*min_lst)