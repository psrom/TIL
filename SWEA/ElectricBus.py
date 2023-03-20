# [S/W 문제해결 기본] 1일차 전기버스
# ========================================
# 종점 도착 못하면 0, 도착하면 최소충전 횟수 출력
# ========================================
# import sys
# sys.stdin = open("sample_input.txt")
T = int(input())

for test_case in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    # K: 충전시 최대 이동가능 정류장 수
    # N: 종점
    # M: 충전기 설치된 정류장 수

    charge_station = list(map(int, input().split()))  # 충전소 위치 리스트
    cnt = current = 0  # 충전 횟수와 현재 위치 초기화

    while (current + K) < N:
        for step in range(K, 0, -1):
            if (current + step) in charge_station:
                current += step
                cnt += 1
                break
        else:
            cnt = 0  # 종점 도달 못할시
            break

    print("#{} {}".format(test_case, cnt))





