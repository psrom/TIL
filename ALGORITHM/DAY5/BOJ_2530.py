# 틀렸던 문제

hour, minute, second = map(int, input().split())
t = int(input())
second += t%60
minute += (second//60 + t//60%60)
hour += (minute//60 + t//60//60)
print(hour%24, minute%60, second%60)