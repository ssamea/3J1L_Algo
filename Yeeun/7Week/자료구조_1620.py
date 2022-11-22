import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}

for i in range(N):
    poketmon = input().strip()
    dic[i+1] = poketmon
    dic[poketmon] = i+1

for _ in range(M):
    question = input().strip()

    if question.isdigit():
        print(dic[int(question)])
    else:
        print(dic[question])


