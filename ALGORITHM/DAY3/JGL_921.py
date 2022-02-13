# a = []
# n = int(input())

# for i in range(1, n+1):
#     square_num = i*i
#     a.append(square_num)

# print(a)

n = int(input())
a = [i*i for i in range(1, n+1)]
print(a)