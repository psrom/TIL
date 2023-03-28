n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = []
def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = (len(lst)+1)//2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    i, j = 0, 0
    lst2 = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            lst2.append(right[j])
            ans.append(right[j])
            j += 1

    while i < len(left):
        lst2.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):
        lst2.append(right[j])
        ans.append(right[j])
        j += 1

    return lst2

merge_sort(a)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)
