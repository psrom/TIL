n = int(input())
set = list(map(int, input().split()))

# def LowerBound(k):
#     start = 0
#     end = len(set)-1
# ===========================================
#     while start < end:
#         mid = int((start+end)/2)
#         if set[mid] < k:
#             start = mid+1
#         else:
#             end = mid
#     return n+1
#
# print(LowerBound(int(input())))