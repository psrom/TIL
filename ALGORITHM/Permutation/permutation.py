# 123 순열 만들기(재귀)
num_lst = [1, 2, 3]
visit = [0 for _ in range(len(num_lst))]
answer = []

def permutation(cnt, arr):
    if cnt == len(num_lst):
        answer.append(arr[:])
        return

    for i, val in enumerate(num_lst):
        if visit[i] == 1:
            continue
        arr.append(val)
        visit[i] = 1

        permutation(cnt+1, arr)
        arr.pop()
        visit[i] = 0

permutation(0, [])

for k in range(len(answer)):
    print(answer[k])
