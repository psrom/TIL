n = input()

if len(n) < 3:
    print(n)
else:
    numbers = list([i for i in range(100, int(n) + 1)])
    cnt = 0
    for num in numbers:
        lst = []
        for i in str(num):
            lst.append(int(i))
        if (lst[2]-lst[1]) == (lst[1]-lst[0]):
            cnt += 1
    if len(n) >= 3:
        print(99+cnt)
