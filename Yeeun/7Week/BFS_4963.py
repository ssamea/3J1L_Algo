from collections import deque

# [h][w]
# 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
result = []


def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        ny, nx = q.popleft()
        for k in range(8):
            yy = ny + dy[k]
            xx = nx + dx[k]
            if 0 <= yy < h and 0 <= xx < w:
                if graph[yy][xx] == 1 and visited[yy][xx] == False:
                    visited[yy][xx] = True
                    q.append((yy, xx))


# 둘 다 0일 때 입력 멈춤
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    cnt = 0
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    for j in range(h):
        for i in range(w):
            if graph[j][i] == 1 and visited[j][i] == False:
                visited[j][i] = True
                bfs(j, i)
                cnt += 1
    result.append(cnt)

for i in result:
    print(i)

