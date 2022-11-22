from collections import deque


def bfs(x):
    q.append(x)
    c = [-1 for _ in range(N)]
    c[x] = 0
    while q:
        x = q.popleft()
        for i in friend[x]:
            if c[i] == -1:
                c[i] = c[x] + 1
                q.append(i)
    cnt = 0
    for i in range(N):
        if c[i] != -1:
            cnt += c[i]
    return cnt


N, M = map(int, input().split())  # 유저수, 관계수
friend = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    A -= 1;
    B -= 1
    friend[A].append(B)
    friend[B].append(A)

q, res, ans = deque(), [], []

for i in range(N):
    res.append(bfs(i))

for i in range(N):
    if res[i] == min(res):
        ans.append(i)

print(min(ans) + 1)

