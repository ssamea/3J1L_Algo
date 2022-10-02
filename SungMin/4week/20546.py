n = int(input())
duck = list(map(int, input().split()))

a, b = n, n
a1, b1 = 0, 0

for i in duck:
    if a >= i:
        a1 += a // i
        a %= i

for i in range(len(duck) - 3):
    if duck[i] > duck[i + 1] > duck[i + 2]:
        b1 += b // duck[i + 3]
        b %= duck[i + 3]

    elif duck[i] < duck[i + 1] < duck[
        i + 2]:
        b += a1 * duck[i + 3]
        s_stock = 0

j_asset = [b + (duck[-1] * a1)]  #
s_asset = [a + (duck[-1] * b1)]  #

if j_asset > s_asset:
    print('BNP')
elif j_asset < s_asset:
    print('TIMING')
else:
    print('SAMESAME')