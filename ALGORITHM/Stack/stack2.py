# 2. 괄호의 짝을 검사하는 프로그램 작성
test_lst = list(map(str, input()))
lst = []

def push(e):
    lst.append(e)

def pop():
    if len(lst) != 0:
        del lst[-1]

cnt = 0
for i in test_lst:
    if i == "(":
        push(i)
    elif (i == ")") & (len(lst) != 0):
        pop()
        cnt += 1


if len(lst) != 0:
    print("False")
elif (cnt != (test_lst.count(")"))) & (len(lst) == 0):
    print("False")
else:
    print("True")