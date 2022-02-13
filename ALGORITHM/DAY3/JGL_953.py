record = input().split()
foul = {}

for name in record:
    foul[name] = record.count(name)

min_foul = min(foul.values())

for key, val in foul.items():
    if val == min_foul:
        print(key)

print(min_foul)