import sys

N = int(sys.stdin.readline())

dp = [-1] * 1001

dp[1] = 1 # SK
dp[2] = 0 # CY
dp[3] = 1 # SK

for i in range(4, N+1):
  if dp[i-1] == 1 or dp[i-3] == 1:
    dp[i] = 0
  else:
    dp[i] = 1

if dp[N] == 1:
  print("SK")
else:
  print("CY")