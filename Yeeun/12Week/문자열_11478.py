import sys
input = sys.stdin.readline

S = input().strip()

word = set()

for i in range(len(S)):
  for j in range(i, len(S)):
    temp = S[i:j+1]
    word.add(temp)
print(len(word))

