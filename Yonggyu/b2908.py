nums = input().split(' ')
list = []
for i in range(len(nums)):
    string = nums[i]
    s =''
    for j in range(len(string)-1,-1,-1):
        s += string[j]
    list.append(s)
max = list[0];
for i in range (len(list)):
    if(max < list[i]):
        max = list[i]

print(max)