scores = [list(map(int,input().split())) for _ in range(5)]
success = 0

for score in scores:
    avg = sum(score)/4
    if avg >= 80:
        success += 1
        print('pass')
    else:
        print('fail')

print(f'Successful : {success}')

# 2
scores = [list(map(int,input().split())) for _ in range(5)]
success = 0
for i in range(5):
    total = 0
    for j in range(4):
        total += score[i][j]
    average = total/4
    if average >= 80:
        success += 1
        print("pass")
    else:
        print("fail")
    
print(f'Successful : {success}')