# 최댓값을 찾고, 몇 번째 수인지 출력
numbers = []
for i in range(9):
    n = int(input())
    numbers.append(n)

print(max(numbers))
print(numbers.index(max(numbers))+1)