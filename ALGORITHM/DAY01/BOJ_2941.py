# 크로아티아 알파벳 문제

word = input()
cro_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro_alphabet:
    if i in str(word):
        word = word.count(i)