import sys

word = sys.stdin.readline().rstrip()
croatians = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatians:
    if i in word:
        word = word.replace(i, '*')

print(len(word))