#문자열에는 reverse라는 메서드(함수)가 존재하지 않습니다.
# 따라서 문자열을 리스트로 타입을 변환한 다음 reverse 함수를 이용
# 그 후 리스트를 다시 join 함수를 이용해서 문자열로 만들어 주면 됩니다.
word = list(input())
result = []

for i in range(1, len(word) -1):
  for j in range(i+1, len(word)):
    first = word[:i]
    second = word[i:j]
    third = word[j:]
    first.reverse()
    second.reverse()
    third.reverse()
    result.append(first + second + third)

result.sort()

print(''.join(result[0]))