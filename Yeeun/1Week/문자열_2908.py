# 2908 상수

import sys

A, B = map(str, sys.stdin.readline().split())

list_A = list(map(int, str(A)))
list_A.reverse()
list_B = list(map(int, str(B)))
list_B.reverse()


A = "".join(map(str, list_A))
B = "".join(map(str, list_B))

if int(A) > int(B):
    print(A)
else:
    print(B)

