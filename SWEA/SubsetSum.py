# 4837. 부분집합의 합
# A = set([1~12])
# 출력: N개의 원소를 가지고 있고, 원소의 합이 K인 부분집합의 개수
# 없을 시 0 출력
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    # N: 부분집합 원소의 개수
    # K: 원소의 합
    A = [i for i in range(1, 13)]
    cnt = 0
    subset = [[]]
    # 모든 부분집합 구하기
    for element in A:
        for l in range(len(subset)):
            subset.append(subset[l] + [element])

    # 조건에 맞는 경우 구하기
    for i in range(len(subset)):
        if (len(subset[i]) == N) & (sum(subset[i]) == K):
            cnt += 1
    print(f"#{test_case} {cnt}")

# ============================================
# 모든 부분집합 구하기(비트 연산)
# ============================================
# for i in range(1<<12):
#     subset = []
#     subset_sum = 0
#     for j in range(12):
#         if i & (1<<j):  # i에서 j번째 비트가 1이면 리턴
#             subset.append(A[j])
#             subset_sum += A[j]
#     # 부분집합 원소의 개수 N, 합 K인 경우
#     if (len(subset) == N) & (subset_sum == K):
#         cnt += 1
