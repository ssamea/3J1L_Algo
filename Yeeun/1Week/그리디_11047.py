import sys

N, K = map(int, sys.stdin.readline().split())

coin = []

for i in range(N):
    coin.append(int(sys.stdin.readline()))

K_tmp = K
min = 0

#인덱스가 N-1인 것에서 부터 0까지 탐색
for i in range(N-1, -1, -1):
    if coin[i] > K_tmp:
        continue
    else:
        min += int(K_tmp / coin[i])
        K_tmp = int(K_tmp % coin[i])

print(min)