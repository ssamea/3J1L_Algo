import sys
n, m = input().split()
numlist = []
money = int(m)
result = 0
for i in range(int(n)):
     numlist.append(int(sys.stdin.readline()))
for i in range(len(numlist)-1,-1,-1):
    num = numlist[i]
    if(money % num != money):
        result+=int(money/num)
        money=money%num
    if(money == 0):
        break
print(result)