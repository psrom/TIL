n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))


for f in find:
    s, e = 0, n-1
    isCard = False
    while s <= e:
        mid = (s + e) // 2
        if f == cards[mid]:
            isCard = True
            break
        elif f > cards[mid]:
            s = mid + 1
        else:
            e = mid - 1
    print(1 if isCard else 0, end=' ')
