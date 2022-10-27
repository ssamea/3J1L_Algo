N = int(input())
a, b = map(int, input().split())
M = int(input())
relation = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0
result = 0

def dfs(a):
  global cnt
  global result
  visited[a] = True
  for i in range(1, N+1):
    if relation[a][i] == 1 and visited[i] == False:
      cnt += 1
      if i == b:
        result = cnt
      dfs(i)
      cnt -= 1


for _ in range(M):
  x, y = map(int, input().split())
  relation[x][y] = relation[y][x] = 1

dfs(a)

if result == 0:
  print(-1)
else:
  print(result)


