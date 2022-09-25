import sys

#deque 라이브러리 불러오기
from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    row, col = list(map(int, sys.stdin.readline().split()))
    graph[row].append(col)

#[[], [2,3], [3,4], [], []]

distance =  [-1] * (N+1)
distance[X] = 0 #출발도시 X는 방문할테니까 0 으로 변경

queue = deque()
queue.append(X)

#큐가 빌 때 까지 반복
while queue:
    now = queue.popleft() #현재 도시 값

    #현재 도시에서 이동가능한 모든 도시 확인하기
    for next in graph[now]:
        #아직 방문하지 않았다면
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

#최단 거리가 K인 도시가 나타나지 않을때는 -1을 출력해야하기  때문에 False로 초기화
check = False

for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if check ==  False:
    print(-1)