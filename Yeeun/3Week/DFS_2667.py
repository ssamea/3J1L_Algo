#위 -> 아래 방식의 DFS
#"앞으로 찾아야 가야할 노드"와 "이미 방문한 노드"를 기준으로 데이터를 탐색

import sys

N = int(input())

graph = [0 for _ in range(N)]
num = []

for i in range(N):
  graph[i] = list(map(int, input()))

#좌우상하

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


count = 0
result = 0

def DFS(x, y):
  if x < 0 or x >= N or y < 0 or y >= N:
    return False
  if graph[x][y] == 1:
    global count
    count += 1
    graph[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      DFS(nx, ny)
    return True
  return False


for i in range(N):
  for j in range(N):
    if DFS(i, j) == True:
      num.append(count)
      result += 1
      count = 0

num.sort()
print(result)

for i in range(len(num)):
  print(num[i])