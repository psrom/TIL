dwarf = list(int(input()) for _ in range(9))
d = sum(dwarf) - 100
one, two = 0, 0

for i in range(len(dwarf)):
    for j in range(i+1, len(dwarf)):
        if dwarf[i]+dwarf[j] == d:
            one = dwarf[i]
            two = dwarf[j]

dwarf.remove(one)
dwarf.remove(two)
dwarf.sort()

for i in dwarf: print(i)
