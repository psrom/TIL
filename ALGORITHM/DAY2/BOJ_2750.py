n = int(input())
for _ in range(n):
    numbers = map(int, input().split("\n"))
    print(sorted(numbers))