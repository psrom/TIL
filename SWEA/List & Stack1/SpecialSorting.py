# 4843. 특별한 정렬
# 출력 띄어쓰기 잘못해서 틀림

T = int(input())
for test_case in range(1, 1+T):
    n = int(input())
    num_lst = list(map(int, input().split()))
    sort_lst = sorted(num_lst)

    special_lst = []
    l = len(sort_lst)
    for i in range(5):
        special_lst.append(sort_lst[l-i-1])
        special_lst.append(sort_lst[i])

    print(f"#{test_case}",*special_lst, sep=' ')
