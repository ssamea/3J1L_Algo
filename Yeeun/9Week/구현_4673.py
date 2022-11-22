num = set(range(1, 10001))
new_num = set()

for i in range(1, 10001):
  for j in str(i):
    i += int(j)
  new_num.add(i)


self_num = sorted(num - new_num)

print(*self_num, sep= '\n')