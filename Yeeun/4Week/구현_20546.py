import sys

money = int(input())
stock = list(map(int, sys.stdin.readline().split()))

jh_money, sm_money = money, money
jh_num, sm_num = 0, 0

#준현 비교
for i in range(14):
    if stock[i] <= jh_money:
        jh_num += int(jh_money / stock[i])
        jh_money = int(jh_money % stock[i])

#성민 비교
for i in range(len(stock) - 3):
    if stock[i] > stock[i+1] > stock[i+2]:
        sm_num += sm_money // stock[i+3]
        sm_money %= stock[i+3]
    elif stock[i] < stock[i+1] < stock[i+2]:
        sm_money += sm_num * stock[i+3]
        sm_num = 0


#자산 계산 : 현재 가지고 있는 현금 + 14일의 주가 * 주식수
jh_assets = jh_money + stock[13] * jh_num
sm_assets = sm_money + stock[13] * sm_num


if jh_assets > sm_assets:
    print("BNP")
elif jh_assets < sm_assets:
    print("TIMING")
else:
    print("SAMESAME")

# import sys
#
# money = int(input())
# stock = list(map(int, sys.stdin.readline().split()))
# jh_money = money
# sm_money = money
# temp = stock[0]
# up = 0
# down = 0
# jh_num = 0
# sm_num = 0
#
# #준현 비교
# for i in range(14):
#     if stock[i] <= jh_money:
#         jh_num += int(jh_money / stock[i])
#         jh_money = int(jh_money % stock[i])
#
# #성민 비교
# for i in range(1, 14):
#     if temp < stock[i]:
#         up += 1
#         temp = stock[i]
#         if up == 3 and sm_num > 0:
#             up = 0
#             sm_money += int(sm_num * stock[i])
#             sm_num = 0
#
#     elif temp > stock[i]:
#         down += 1
#         temp = stock[i]
#         if down >= 3 and stock[i] <= sm_money:
#             sm_num += int(sm_money / stock[i])
#             sm_money = int(sm_money % stock[i])
#
#     else:
#         up = 0
#         down = 0
#         temp = stock[i]
#
#
#
# #자산 계산 : 현재 가지고 있는 현금 + 14일의 주가 * 주식수
# jh_assets = jh_money + stock[13] * jh_num
# sm_assets = sm_money + stock[13] * sm_num
#
#
# if jh_assets > sm_assets:
#     print("BNP")
# elif jh_assets < sm_assets:
#     print("TIMING")
# else:
#     print("SAMESAME")