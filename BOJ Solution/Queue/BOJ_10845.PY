n = int(input())
lst = list([input().split(" ") for _ in range(n)])
result = []

for i in range(len(lst)):
    if lst[i][0] == "push":
        result.insert(0, lst[i][1])
    elif lst[i][0] == "pop":
        if result:
            p = result.pop()
            print(p)
        else:
            print(-1)
    elif lst[i][0] == "size":
        print(len(result))
    elif lst[i][0] == "empty":
        if result:
            print(0)
        else:
            print(1)
    elif lst[i][0] == "front":
        if result:
            print(result[len(result)-1])
        else:
            print(-1)
    else:
        if result:
            print(result[0])
        else:
            print(-1)
