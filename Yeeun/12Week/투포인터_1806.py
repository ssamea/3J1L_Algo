N, S = map(int, input().split())

num = list(map(int, input().split()))

target, left, right = 0, 0, 0
answer = 100001
while True:
    if target >= S:
        answer = min(answer, right - left)
        target -= num[left]
        left += 1
    else:
        if right == N:
            break

        target += num[right]
        right += 1

if answer == 100001:
    print(0)
else:
    print(answer)