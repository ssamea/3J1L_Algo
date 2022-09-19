import sys

N = int(sys.stdin.readline())

Fibo = [0] * (N + 1)

Fibo[0] = 0
Fibo[1] = 1

for i in range(2, N + 1):
    Fibo[i] = Fibo[i - 1] + Fibo[i - 2]

print(Fibo[N])