# str = input()
#
# zero_cnt = 0
# one_cnt = 0
#
# for i in str:
#     if i == '0':
#         zero_cnt += 1
#     else:
#         one_cnt += 1
# new_str = []
#
# for i in range(zero_cnt // 2):
#     new_str.append("0")
#
# for i in range(one_cnt // 2):
#     new_str.append("1")
#
# new_str.sort()
#
# print(''.join(new_str))

#위의 코드로 진행시 25점 나옴
#반례 00110000 -> 0010이 나와야 하는데 0001 출력
#--------
str = list(input())

zero_cnt, one_cnt = str.count('0') // 2, str.count('1') // 2

#문자열의 순서를 유지하면서 제거해야하기 때문에 서로 다른 방향으로 지워주면 된다.

for _ in range(one_cnt):
    str.pop(str.index('1')) #index()는 리스트 중에서 특정한 원소가 몇 번째에 처음으로 등장했는지 알려주는 함수

for _ in range(zero_cnt):
    str.pop(-str[::-1].index('0')-1)

print(''.join(str))

'''
시작 인덱스와 끝 인덱스를 생략하면서 인덱스 증가폭을 -1로 지정하면 어떻게 될까요? 이때는 리스트 전체에서 인덱스를 1씩 감소시키면서 요소를 가져오므로 리스트를 반대로 뒤집습니다.
>>> a[::-1]
[90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
'''