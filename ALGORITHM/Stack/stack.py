# 스택 구현
# push, pop 구현

stack_lst = []

def push(e):
    stack_lst.append(e)
    print(stack_lst)

def pop():
    del stack_lst[-1]
    print(stack_lst)



for i in range(1, 4):
    push(i)

for _ in range(1, 4):
    pop()