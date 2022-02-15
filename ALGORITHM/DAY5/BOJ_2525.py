h, m = map(int,input().split())
need_time = int(input())
total_minute = m+need_time

if total_minute <= 59:
    if h <=23:
        print(h, total_minute, sep=" ")
else:
    cal_minute = total_minute%60
    cal_hour = total_minute//60
    if h+cal_hour >= 24:
        calc_hour = (h+cal_hour)%24
        print(calc_hour, cal_minute, sep=" ")
    else:
        print(cal_hour+h, cal_minute, sep=" ")