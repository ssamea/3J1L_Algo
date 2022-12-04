from collections import deque

N, M, V = map(int, input().split())
# 정점 개수, 간선 개수, 시작 번호
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)


def dfs(v):
    visited1[v] = True
    print(v, end=" ")
    for i in range(1, N + 1):
        if graph[v][i] == 1 and visited1[i] == False:
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if graph[v][i] == 1 and visited2[i] == False:
                q.append(i)
                visited2[i] = True


for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(V)
print()
bfs(V)