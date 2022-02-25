countries = {}

for _ in range(int(input())):
    country, capital = input().split()
    countries[country] = capital

print(countries.get(input(), 'Unknown Country'))