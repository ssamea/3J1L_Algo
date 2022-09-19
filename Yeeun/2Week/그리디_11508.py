import sys

N = int(sys.stdin.readline())

product = []

min = 0
#sys.setrecursionlimit(100000)

#1부터 N까지의 값 넣기

for i in range(N):
    product.append(int(sys.stdin.readline()))

product.sort(reverse=True)
#내림차순으로 큰수부터 정렬해야 3개씩 묶었을 때 제일 끝에 있는 수가 젤 저렴한 가격


#가장 작은 것 순으로  묶기
for i in range(0, N, 3):
    if i == N-1:
        min += product[i]
    else:
        min += product[i] + product[i + 1]
print(min)