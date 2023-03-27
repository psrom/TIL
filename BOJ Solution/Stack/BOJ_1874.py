# 스택 수열
# push 연산은 +로, pop 연산은 -로 표시
# 불가능할 경우 NO 출력
stack = []
ans = []
cnt = 1
tmp = True

for _ in range(int(input())):
    num = int(input())
    # push
    while cnt <= num:
        stack.append(cnt)
        ans.append("+")
        cnt += 1
    # pop
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else: tmp = False

if not tmp: print("NO")
else:
    for i in ans:
        print(i)









































