# 함께 문제 푸는 날짜가 겹치는 경우
a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0:
    d += 1
print(d)