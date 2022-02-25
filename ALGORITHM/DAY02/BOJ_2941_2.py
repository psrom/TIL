word = input()
changes = ['=', '-', 'lj', 'nj', 'dz=']
total = len(word)

for change in changes:
    total -= word.count(change)
print(total)