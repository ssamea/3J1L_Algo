import sys

N = int(input())
people = []

for i in range(N):
    name, k, e, m = sys.stdin.readline().split()
    people.append([name, int(k), int(e), int(m)])

#-내림차순
# arr.sort(key = lambda x : x[1], reverse=True) == arr.sort(key=lambda x : -x[1])

people.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]) )

for i in people:
    print(i[0])