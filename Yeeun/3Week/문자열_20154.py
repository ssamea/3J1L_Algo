import sys

#개행문자 제거를 위해 strip() 꼭 포함 시키기
S = sys.stdin.readline().strip()

alphabet = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

battle = []

for letter in S:
  idx = ord(letter) - 65
  battle.append(alphabet[idx])

result = sum(battle) % 10

#1이면 홀수이고 true이니까
if result % 2:
  print("I'm a winner!")
else:
  print("You're the winner?")