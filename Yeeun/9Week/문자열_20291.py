import sys

input = sys.stdin.readline

N = int(input())

extension = {}

for _ in range(N):
    file = input().strip()
    name = file.split('.')
    if extension.get(name[1]):
        extension[name[1]] += 1
    else:
        extension[name[1]] = 1

extension = dict(sorted(extension.items()))

for key, value in extension.items():
    print(key, value)


