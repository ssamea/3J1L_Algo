import sys

S = sys.stdin.readline().rstrip()
#rstrip : 문자열에 오른쪽 공백이나 인자가된 문자열의 모든 조합을 제거
alphabet = [0]*26

for i in S:
    alphabet[ord(i)-97] += 1
#ord()는 ord(문자)를 숫자로 나타내주는 함수

for value in alphabet:
    print(value, end=' ')
# 한줄에 띄어쓰고 출력하려면 end = ' '
# 그냥 print만 하는게 end='/n'과 같음

#print(*alphabet)
#위에 작성한 출력 for문을 한줄로 표현할 수 있음

"""
Traceback (most recent call last):
  File "/Users/yeaeun/PycharmProjects/Python_Algo/Yeeun/2Week/문자열_10808.py", line 8, in <module>
    alphabet[ord(i)-97] += 1
IndexError: list index out of range
"""
#S = sys.stdin.readline()으로 작성했을 때 에러가 뜸
