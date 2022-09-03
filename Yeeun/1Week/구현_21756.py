import sys

N = int(sys.stdin.readline())

array = []
#1부터 N까지의 값 넣기
for i in range(1, N+1):
    array.append(i)

while(len(array) != 1):
    #홀수번째 제거인데 인덱스 0부터 시작하니까 짝수번째 값을 0으로 바꾸고 0이 들은 값 제거로 구현
    for i in range(0, len(array)):
        if i % 2 == 0:
            array[i] = 0

    #0이 들은 값 제거
    remove_set = {0}
    #while 0 in array: array.remove(0) 으로도 지울 수 있지만, 시간복잡도가 O(N)이므로
    #아래와 같은 방법으로 사용하면 나중에 시간 절약을 할 수 있음
    #remove_set에 없는 데이터만 새로운 리스트에 저장하여 특정 값을 제거하는 효과
    array = [i for i in array if i not in remove_set]



print(array[0])


