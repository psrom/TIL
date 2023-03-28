# 주유소
# 각 도시마다 주유소가 있고, 최소 비용으로 목적지에 도달하는 방법 찾기
n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
m = price[0]
for i in range(n-1):
    if price[i] < m:
        m = price[i]
    result += m * road[i]

print(result)
