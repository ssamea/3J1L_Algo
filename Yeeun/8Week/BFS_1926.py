from collections import deque
N, M = map(int, input().split())
#N 세로 M 가로

map = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cnt = 0
maxValue = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x):
    result = 1
    q = deque()
    q.append((y,x))
    while q:
        y1, x1 = q.popleft()
        for i in range(4):
            ny = dy[i] + y1
            nx = dx[i] + x1

            if 0<=ny<N and 0<=nx<M:
                if map[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    result += 1
                    q.append((ny, nx))

    return result

for j in range(N):
    for i in range(M):
        if map[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            cnt += 1
            maxValue = max(maxValue, bfs(j, i))


print(cnt)
print(maxValue)
