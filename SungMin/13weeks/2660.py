# 플로이드 와샬
import sys
input = sys.stdin.readline

m = int(input())
INF = int(1e9)
graph = [[INF]*(m+1) for _ in range(m+1)] # 그래프 초기화

# 자기 자신은 0으로 초기화
for i in range(1, m+1):
    for j in range(1, m+1):
        if i == j:
            graph[i][j] = 0

# 입력
while True:
    a, b = map(int,input().split())

    # 마지막 줄이 -1이면 입력 종료
    if a == -1 and b == -1 :
        break

    # 친구 관계
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드 와샬 알고리즘
for k in range(1, m+1):
    for a in range(1, m+1):
        for b in range(1, m+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 회장은 회원들 중에서 점수가 가장 작은 사람
score = [] # 회장 후보 점수 리스트
res = []  # 회장 후보

for i in range(1, m+1):
    score.append(max(graph[i][1:]))

ans_score = min(score)

for i in range(1,m+1):
    if ans_score == max(graph[i][1:]):
        res.append(i)
res.sort()
print(ans_score, len(res))
for i in res:
    print(i, end=" ")
