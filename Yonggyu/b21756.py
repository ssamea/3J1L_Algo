num = int(input())
lst = list(range(1,num+1))
tmp=lst
result = 0
while len(tmp) != 1:
    nlst =[]
    for i in range(len(tmp)):
        if(i % 2 == 1):
            nlst.append(tmp[i])
    tmp = nlst
print(tmp[0])