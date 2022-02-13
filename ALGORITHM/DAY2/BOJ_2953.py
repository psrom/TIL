total = []
for i in range(5):
    score = (map(int, input().split()))
    total.append(sum(score))
print(total.index(max(total))+1,max(total))