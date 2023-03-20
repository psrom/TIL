# 4871. [파이썬 S/W 문제해결 기본] 4일차-그래프 경로
# DFS 알고리즘

def dfs(S, G):
    stack = []
    stack.append(S)

    while stack:
        v = stack.pop()

        if visit[v] == 0:
            visit[v] = 1

            for w in range(1, V+1):
                if (graph[v][w] == 1) and (visit[w] == 0):
                    if w == G:
                        return 1
                    stack.append(w)
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    visit = [0 for _ in range(V+1)]
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1

    S, G = map(int, input().split())
    print(f"#{tc} {dfs(S, G)}")
