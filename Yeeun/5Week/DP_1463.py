# 이 문제는, 전의 결과를 다음 결과에 이용하게 되는 점화식을 활용한 DP 문제이다.
# X = 10인 경우, 10 -> 9 -> 3 -> 1 과정을 거쳐 1이 되게 되는데
# 9의 경우에는 또, 9 -> 3 -> 1의 과정을 거치며 3의 경우에는 3 -> 1의 과정을 거친다.
# 즉, 10을 구할 때는 9의 결과를, 9를 구할 때는 3의 결과를 이용한다.
# 앞에서 구한 결과값을 저장하였다가 후에 사용하는 것이다.

N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 #6에서 1을 빼면 5다 따라서 dp[6]은 dp[5]의 횟수에 1을 빼는 행동 하나만 추가해주면 된다

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])

