# 알파벳 소문자로만 이루어진 단어
n = input() # 첫째 줄에 단어 S
n.lower() # 소문자처리
alphabet = [0]*26 # 알파벳 26개 0으로 초기화


for i in n:
    alphabet[ord(i)-97] = n.count(i) # ord함수로 정수처리해서 갯수를 셈

for i in alphabet:
    print(i, end = ' ')
