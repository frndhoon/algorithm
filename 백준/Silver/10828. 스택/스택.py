import sys
input = sys.stdin.readline
cnt = int(input())
stack = []

for _ in range(cnt):
    command = input().split()
    cmd = command[0]

    if cmd == 'push':
        stack.append(command[1])

    elif cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print("-1")

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'empty':
        if not stack:
            print("1")
        else:
            print("0")

    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print("-1")

