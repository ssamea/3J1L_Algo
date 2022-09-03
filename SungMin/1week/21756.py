import sys
input=sys.stdin.readline
n = int(input())
arr = []
temp = []

for i in range(0, n):
    arr.append(i+1)
#print(arr)

# (A) 홀수번 칸의 수들을 모두 지운다
# (B) 남은 수들을 왼쪽으로 모은다.
# => 반복문으로 돌린다
while len(arr) != 1:
    for i, v in enumerate(arr):
        if i % 2 != 0:
            temp.append(v)
    arr = temp #  중간 중간 값이 변하는 임시 배열로 바꿔주기
    #print(arr)
    temp = [] # 초기화
print(arr[0])