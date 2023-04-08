# ==============================================================================
# 시간초과 난 이유: result를 리스트로 받아서 sum(lst)로 더하는 과정이 시간초과 난 걸로 추정
# end point를 sum(trees)로 잡고 result를 바로 구해서 과정 단축 => solve!
# ==============================================================================
# n: 나무의 수, m: 가져가려고 하는 나무의 길이
# 나무들의 높이
n, m = map(int, input().split())
trees = list(map(int, input().split()))
s, e = 1, sum(trees)

while s <= e:
    mid = (s+e)//2
    result = 0 # 잘린 나무 길이의 합

    for tree in trees:
        if tree > mid:
            result += tree-mid

    if result >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)
