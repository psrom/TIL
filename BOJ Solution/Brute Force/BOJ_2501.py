n, k = map(int, input().split())
n_lst = [i for i in range(1, n+1)]
result = []

for num in n_lst:
    if n%num == 0:
        result.append(num)

if len(result) >= k:
    print(result[k-1])
else:
    print(0)