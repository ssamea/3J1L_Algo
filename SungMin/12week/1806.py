import sys
max = sys.maxsize
N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
tmp = 0
ans = max

while True:
   if tmp >= S:
       ans = min(ans, right - left)
       tmp -= arr[left]
       left += 1

   elif right == N:
       break

   else:
       tmp += arr[right]
       right += 1

if ans == max:
   print(0)
else:
   print(ans)