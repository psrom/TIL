# 부분집합 구하기
# bit = [0] * 4
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

# =============================
# 비트 연산자: 0과 1로 이루어진 이진수에 대한 연산을 수행하는 연산자
# &(AND) |(OR) <<(LEFT SHIFT) >>(RIGHT SHIFT)

# 1 << n: 2^n => 원소가 N개일 경우의 모든 부분 집합의 수
# i & (1<<j): 1 => i에서 j번째 비트가 1인지 아닌지를 리턴
# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i&(1<<j):
#             print(arr[j], end='')
#     print()