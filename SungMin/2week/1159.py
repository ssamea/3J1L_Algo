# 과일우유, 드링킹요구르트 등의 유제품을 '2+1 세일'하는 행사
# 유제품 3개를 한 번에 산다면 그중에서 가장 싼 것은 무료로 지불하고 나머지 두 개의 제품 가격만 지불하면 됩니다.
# 한 번에 3개의 유제품을 사지 않는다면 할인 없이 정가를 지불해야 합니다

n = int(input()) # 유제품의 수
price = []
total = 0 # 총가격
# 유제품의 가격 input
for i in range(n):
    p = int(input())
    price.append(p)


# 1) 3개씩 묶어사는거 구현
price.sort(reverse=True) # ex. (6 5 5) (5 5 4)

for i in range(len(price)):
    if i % 3 != 2: # 비싼 순으로 정렬을 하게 되면 각 3,6,9번째는 작은 값이 되기에 나머지가 2가 아닌값들만 넣어주면됨 -> 인덱스는 0부터 시작이므로 2임
        total += price[i]

print(total)