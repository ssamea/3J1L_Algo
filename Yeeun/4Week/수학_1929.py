import sys
import math

M, N = map(int, sys.stdin.readline().split())


# M부터 판별하는 수(N) 전까지 나눠보고 나머지가 0이 안나온다면 소수로 정의

# num의 제곱값으로 확인
def prime_num(num):
    if num == 1: return False
    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:
            return False
    return True


for idx in range(M, N + 1):
    if prime_num(idx):
        print(idx)