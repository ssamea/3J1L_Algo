# 이 구역의 승자는 누구야?!
#  알파벳 대문자로만 이루어진 문자열이 주어진다 -> 문자열이 주어지면 각 문자의 획수로 문자를 변환 => 근데 문제 보면 걍 각 문자열의 획수를 다 더한거임

k = input()
k.upper() # 대문자 변환

nums = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1] # 각 알파벳 획수
res = []
for i in k:
    temp = ord(i) - ord('A') # 입력값의 알파벳 인덱스 찾기
    res.append(nums[temp])

total = 0

for i in res:
    total+=i

#if total >= 10:
#    total = total % 10
    #print(total)
if total % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")