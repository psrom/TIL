numbers = list(range(1, 10001))
remove_lst = []
for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        remove_lst.append(num)

for remove_num in set(remove_lst):
    numbers.remove(remove_num)

for self_num in numbers:
    print(self_num)
