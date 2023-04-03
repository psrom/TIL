def dfs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return dfs(n-1)+dfs(n-2)+dfs(n-3)

for _ in range(int(input())):
    n = int(input())
    print(dfs(n))
