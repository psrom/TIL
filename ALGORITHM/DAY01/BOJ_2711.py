# T=int(input())

# for i in range(T):
#     n,word=(input().split())
#     n = int(n)
#     print(word[:n-1]+word[n:])

for _ in range(int(input)):
    index, word = (input().split())
    index = int(index)
    print(word[:index-1]+word[index:])