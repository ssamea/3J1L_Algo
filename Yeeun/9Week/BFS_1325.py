from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(start):
    cnt = 1
    visited = [False] * (N + 1)

    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        cur = q.popleft()
        for nx in graph[cur]:
            if not visited[nx]:
                visited[nx] = True
                cnt += 1
                q.append(nx)
    return cnt


maxCnt = 1
ans = []

for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > maxCnt:
        maxCnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == maxCnt:
        ans.append(i)

print(*ans)
