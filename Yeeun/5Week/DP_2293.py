"""
    1 2 3 4 5 6 7 8 9 10
 1  1 1 1 1 1 1 1 1 1 1
 2  0 1 1 2 2 3 3 4 4 5
 5  0 0 0 0 1 1 2 2 3 4
 S  1 2 2 3 4 5 5 7 8 10
 ex) 2원으로 4원을 만들 때 2원을 만드는 경우의 수를 더하면 된다.
"""

import sys

N, K = map(int, sys.stdin.readline().split())

dp = [0] * (K + 1)
coin = []

for i in range(N):
    coin.append(int(input()))

dp[0] = 1 # 1원으로 1원 만들기(1-1), 2원으로 2원 만들기(2-2), 5원으로 5원 만드는(5-5) 경우의 수가 dp[0]인데 이 경우는 모두 1임을 알 수 있음

for i in coin:
    for j in range(i, K+1):
        dp[j] += dp[j - i]




print(dp[K])
