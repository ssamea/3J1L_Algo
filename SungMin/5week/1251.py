n = input()
arr = []
for i in range(len(n)-2):
    for j in range(i+1, len(n)-1):
        for k in range(j+1, len(n)):
            t = n[:j][::-1] + n[j:k][::-1] + n[k:][::-1]
            arr.append(t)
print(min(arr))