def div(n, i, j):
    if n ==0 :
        return

    cnt = (i+j-1)//3

    # 오른쪽
    div(n-1, i, i+cnt-1)
    # 왼쪽
    div(n-1, i+cnt*2, j)
    # 가운데
    for k in range(i+cnt, i+cnt*2):
        ans[k] = " "

while True:
    try:
        n = int(input())
        ans = ["-"] * (3**n)
        div(n, 0, 3**n-1)
        print("".join(ans))
    except:
        break
