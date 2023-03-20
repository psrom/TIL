# 4839. 이진탐색
def BinarySearch(start, end, target, cnt):
    page = (start+end)//2
    if page == target:
        return cnt
    elif target > page:
        return BinarySearch(page, end, target, cnt+1)
    else:
        return BinarySearch(start, page, target, cnt+1)

T = int(input())

for test_case in range(1, T+1):
    P, A, B = map(int, input().split())
    # P: 전체 쪽수
    # A, B: A,B가 각각 찾을 쪽 번호

    result_A = BinarySearch(1, P, A, 0)
    result_B = BinarySearch(1, P, B, 0)

    # 결과 출력
    if result_A > result_B:
        print(f"#{test_case} B")
    elif result_A < result_B:
        print(f"#{test_case} A")
    else:
        print(f"#{test_case} 0")
