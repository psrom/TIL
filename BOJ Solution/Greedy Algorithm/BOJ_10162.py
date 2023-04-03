t = int(input()) # 초단위 시간

a, b, c = 300, 60, 10
cnt_a, cnt_b, cnt_c = 0, 0, 0

if t % 10 != 0:
    print(-1)
else:
    while t != 0:
        if t//a > 0:
            cnt_a = t//a
            t %= a
        elif t//b > 0:
            cnt_b = t // b
            t %= b
        elif t//c > 0:
            cnt_c = t // c
            t %= c
    print(cnt_a, cnt_b, cnt_c)
