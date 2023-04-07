# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    total = brown + yellow
    rows = [total // i for i in range(3, (total) // 3 + 1) if (total) % i == 0]
    # 이 부분의 작동 원리를 잘 이해 못했음
    print(rows)

    for row in rows:
        col = (total) // row
        if 2 * (row + col - 2) == brown:
            return [row, col]
