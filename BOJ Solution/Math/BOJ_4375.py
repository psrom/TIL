while True:
    try:
        n = int(input())
        ans = 0
        i = 0
        while True:
            i += 1
            ans = ans * 10 + 1
            ans %= n
            if ans == 0:
                print(i)
                break
    except:
        break