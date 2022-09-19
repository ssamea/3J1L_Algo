import sys

#제출 여부를 판단하는 boolean 리스트
submit = [0] * 31
no_submit = []

submit[0] = 1

for i in range(28):
    number = int(sys.stdin.readline())
    submit[number] = 1

    # print(number)

for i in range(1, 31):
    if submit[i] == 0:
        no_submit.append(i)

no_submit.sort()

print(no_submit[0])
print(no_submit[1])