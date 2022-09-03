# 입력: 첫째 줄은 재환이가 가장 길게 낼 수 있는  "aaah"이다. 둘째 줄은 의사가 듣기를 원하는 "aah"이다
# 출력: 재환이가 그 병원에 가야하면 "go"를, 아니면 "no"를 출력한다.
a = input() # 재환
b = input() # 의사

if len(a) >= len(b):
    print('go')

else:
    print('no')