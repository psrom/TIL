# 알고리즘 수업 - 깊이 우선 탐색1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 탐색
visited_dfs = [0] * (N+1)
cnt = 1

def dfs(R):
    global cnt
    visited_dfs[R] = cnt
    graph[R].sort()
    for g in graph[R]:
        if visited_dfs[g] == 0:
            cnt += 1
            dfs(g)

dfs(R)
for i in range(1, N+1):
    print(visited_dfs[i])
