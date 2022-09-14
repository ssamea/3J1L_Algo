# 입력
# 첫째 줄에 n이 주어진다. n은 90보다 작거나 같은 자연수이다.
# Fn = Fn-1 + Fn-2 (n ≥ 2)

n = int(input())
dp = [0 for _ in range(n+1)] # 인덷스 0,1 번째 수는 0,1로 고정
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])
