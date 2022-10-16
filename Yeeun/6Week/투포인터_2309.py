people = []

left = 0
right = 8

for i in range(9):
  people.append(int(input()))

people.sort()
#투포인터 비교 시작

result = sum(people) - 100

while True:
  if people[left] + people[right] == result:
    people.remove(people[left])
    people.remove(people[right-1]) # -1해주는 이유는 앞에서 left꺼를 삭제했으니 people 인덱스 수가 1개 줄은 상태임
    break

  elif people[left] + people[right] < result:
    left += 1
  elif people[left] + people[right] > result:
    right -= 1

people.sort()
print(*people, sep = '\n')

