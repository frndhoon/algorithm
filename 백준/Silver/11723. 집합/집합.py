import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    command = input().rstrip()
    if command == 'all':
        arr = [str(i) for i in range(1, 21)]
    elif command == 'empty':
        arr = []
    else:
        cmd, value = list(map(str, command.split()))
        if cmd == "add" and value not in arr:
            arr.append(value)
        if cmd == "check":
            if value in arr:
                print("1")
            else:
                print("0")
        if cmd == "remove" and value in arr:
            arr.remove(value)
        if cmd == "toggle":
            if value in arr:
                arr.remove(value)
            else:
                arr.append(value)
