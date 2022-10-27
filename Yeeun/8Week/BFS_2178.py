from collections import deque
N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

def bfs(x, y):
  q = deque()
  q.append((x, y))

  while q:
    nx, ny = q.popleft()
    for i in range(4):
      yy = ny + dy[i]
      xx = nx + dx[i]
      if 0<= yy<M and 0<=xx<N:
        if graph[xx][yy] == 1:
          q.append((xx, yy))
          graph[xx][yy] = graph[nx][ny] + 1

bfs(0, 0)

print(graph[N-1][M-1])
