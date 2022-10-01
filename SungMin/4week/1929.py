# M이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 에라토테네스의 체= 소수가 아닌 수의 배수들을 모두 제외시키는 방법
import math
m, n = map(int,input().split())

"""
for i in range(m,int(math.sqrt(n))+1):
    if res[i] == True:
        j=2
        while i*j <= n:
            res[i*j]=False
            j+=1
"""
def prime(m):
    #if m==1: return False

    for i in range(2,int(math.sqrt(m))+1):
        if m % i == 0:
            return False

    return True

for i in range(m, n+1):
    if prime(i):
        print(i)

