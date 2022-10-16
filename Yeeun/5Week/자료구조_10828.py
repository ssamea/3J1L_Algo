N = int(input())
stack = []
result = []

for i in range(N):
    command = input()

    if command == "pop":
        if not stack:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif command == "size":
        result.append(len(stack))
    elif command == "empty":
        if not stack:
            result.append(1)
        else:
            result.append(0)
    elif command == "top":
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
    else:
        words = command.split()
        stack.append(int(words[1]))

print(*result, sep='\n')





