# 이진탐색 내장모듈 bisect이용
# bisect_right(list, value): list에서 value가 들어갈 가장 오른쪽 인덱스
# bisect_left(list, value): list에서 value가 들어갈 가장 왼쪽 인덱스
from bisect import bisect_right, bisect_left

n = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()
m = int(input())
m_arr = list(map(int, input().split()))


def count_by_range(x, l_val, r_val):
    r_idx = bisect_right(x, r_val)
    l_idx = bisect_left(x, l_val)
    return r_idx - l_idx

for i in range(len(m_arr)):
    print(count_by_range(n_arr, m_arr[i], m_arr[i]), end=" ")




