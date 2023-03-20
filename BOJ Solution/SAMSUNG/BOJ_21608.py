# 상어 초등학교
from typing import List

# 문제: 학생 만족도의 총 합 구하기

# 조건
# 1. 빈 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리 배정
# 2. 1을 만족하는 칸이 여러 개면, 비어있는 칸이 가장 많은 칸으로 자리 배정
# 3. 2를 만족하는 칸이 여러 개면, 행의 번호 최소, 행도 여러 개면 열의 번호 최소 자리
# =======================================================================
n = int(input())
students = [list(map(int, input().split())) for _ in range(n*n)]
classroom = [[0]*n for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 자리 배정하기
for order in range(n*n):
    student = students[order]
    seat_lst = []
    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr, nc = i+dr[k], j+dc[k]
                    if (0 <= nr < n) and (0 <= nc < n):
                        if classroom[nr][nc] in student[1:]:
                            like += 1
                        elif classroom[nr][nc] == 0:
                            blank += 1
                    seat_lst.append([like, blank, i, j])
    # 자리 배정할 때 like > blank 우선순위
    seat_lst.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    classroom[seat_lst[0][2]][seat_lst[0][3]] = student[0]

# 만족도 검사
result = 0
# 학생 순서대로 점수 주기 위해서 정렬
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nr, nc = i+dr[k], j+dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if classroom[nr][nc] in students[classroom[i][j]-1]:
                    ans += 1
        if ans != 0:
            result += (10 ** (ans-1))
        print(students[classroom[i][j]-1])
print(result)
