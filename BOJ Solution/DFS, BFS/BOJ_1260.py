# DFS, BFS 구현
# 1. 리스트로 구현
# ========================================================
N, M, V = map(int, input().split()) # 정점, 간선, 시작노드

# 행렬 생성
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 행렬
visit_dfs = [0] * (N+1)
visit_bfs = [0] * (N+1)

def dfs(v):
    visit_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, N+1):
        if visit_dfs[i] == 0 and graph[V][i] == 1:
            dfs(i)

def bfs(v):
    # 시작 정점
    queue = [v]
    visit_bfs[v] = 1
    while queue:
        V = queue.pop(0)
        print(V, end=" ")
        for i in range(1, N+1):
            if visit_bfs[i] == 0 and graph[V][i] == 1:
                queue.append(i)
                visit_bfs[i] = 1

dfs(V)
print()
bfs(V)
