#알람 시계(45분 당기기)
h, m = map(int, input().split())

if h == 0 :
    if m < 45:
        print(23, m+15)
    else:
        print(h, m-45)
else:
    if m >= 45:
        print(h, m-45)
    else:
        print(h-1, m+15)