from collections import deque
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    d = deque(list(map(int, input().split())))
    cnt = 0

    while d:
        max_v = max(d)
        front = d.popleft()
        m -= 1 # 위치 앞당기기

        if max_v == front: # 최댓값을 뽑았을 때 count 추가
            cnt += 1
            if m == -1:
                print(cnt) # 나의 숫자를 뽑음
                break
        else:
            d.append(front) # 최댓값을 뽑은 게 아님 => 뒤로 보냄
            if m == -1:
                m = len(d) - 1 # 맨 뒤로 이동














