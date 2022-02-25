# 1, 2, 3, ... 순서대로 더해 합을 만들 때 입력 받은 정수보다 작을 동안만 더함
# 입력받은 정수보다 같거나 커진 경우를 출력
n = int(input())
s = 0
c = 0
while True:
    s += c
    c += 1
    if s >= n:
        break
print(s)
