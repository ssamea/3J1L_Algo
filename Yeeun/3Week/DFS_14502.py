import sys

N = int(input()) #세로
M = int(input()) #가로

graph = [0 for _ in range(N)]
num = []

for i in range(N):
    graph[i] = list(map(int, input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

min = 987654321
global count
count = 0

def DFS(x, y):

    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if count == 3:
        return False
    if graph[x][y] == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 0:
                count += 1
                graph[nx][ny] = 1
                DFS(nx, ny)
        return True
    return False


