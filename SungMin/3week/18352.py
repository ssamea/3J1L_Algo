from collections import deque
import sys
input=sys.stdin.readline
def bfs(start,k):
    q=deque()
    q.append(start)

    while q:
        now = q.popleft()

        for i in arr[now]:
            if dist[i]==-1:
                dist[i] = dist[now]+1
                q.append(i)


n,m,k,x=map(int,input().split()) # 도시, 도로 개수, 거리 정보, 출반도시번호
arr = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)

dist = [-1] * (n+1)  # 각 도시에 대한 거리정보. 미방문 상태를 -1로 설정
dist[x] = 0  # 출발 도시까지 거리는 0

bfs(x, k)
# 최단 거리 찾기
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        #check=True

if k not in dist:
    print(-1)