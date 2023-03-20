# 4869. [파이썬 S/W 문제해결 기본] 4일차-종이 붙이기

def paper(size):
    # a0 case
    if size == 10:
        return 1
    elif size == 20:
        return 3
    else:
        return paper(size-20) * 2 + paper(size-10)

T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    print(f"#{test_case} {paper(size)}")
