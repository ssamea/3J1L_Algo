import sys
input=sys.stdin.readline

student = list(map(int,range(1,31))) # 30명 학생

for i in range(0, 28):
    n = int(input())
    if n in student: # 학생 리스트에 있으면 소거
        student.remove(n)

student.sort()
for i in student:
    print(i)
