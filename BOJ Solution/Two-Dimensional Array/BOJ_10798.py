# 세로읽기
# 5줄의 입력

lst = [list(input()) for _ in range(5)]
length = [len(word) for word in lst] # 문자 길이 행렬
ans = ''

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            ans += lst[j][i]

print(ans)
