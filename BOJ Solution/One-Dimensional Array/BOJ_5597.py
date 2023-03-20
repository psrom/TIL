# 과제 안 낸 사람 찾기
N = 28
# 학생 수 만큼 배열 만들기
student_arr = [0 for i in range(N+2)]

for i in range(N):
    student_num = int(input())
    student_arr[student_num-1] = 1

for i, v in enumerate(student_arr):
    if v == 0:
        print(i+1)