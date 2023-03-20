# [S/W 문제해결 기본] 1일차 min max
# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력

T = int(input())
for test_case in range(T):
    input()
    lst_temp = list(map(int, input().split()))
    result = max(lst_temp) - min(lst_temp)

    print(f"#{test_case+1} {result}")
