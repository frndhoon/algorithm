import sys
input = sys.stdin.readline

n = input()
arr = []
orders = list(map(int, input().split()))

for num, order in enumerate(orders):
    num = num + 1
    arr.insert(num - order - 1, num)

print(*arr, end=" ")