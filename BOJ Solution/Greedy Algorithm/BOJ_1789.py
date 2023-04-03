s = int(input())

x = 1
while True:
    if x*(x+1)/2 > s:
        print(x-1)
        break
    else:
        x += 1
