# 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다
# 게임은 상근이가 먼저 시작한다.
n = int(input())

# 상근이가 첫빠따니까 홀수번임
if n%2 == 1:
    print("SK")
else:
    print("CY")