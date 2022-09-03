import sys
input=sys.stdin.readline
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

# 출력
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

n, k = map(int, input().split())
Ai = []
cnt = 0

# 한줄씩 받으라해서 귀찮아
for i in range(n):
    Ai.append(int(input()))

Ai.sort(reverse=True)

# 가장 높은 금액부터 나눠지는지 카운터
for i in range(len(Ai)):
    if k // Ai[i] == 0:
        continue
    else :
        cnt += k // Ai[i]
        k = k % Ai[i]

print(cnt)