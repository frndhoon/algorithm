import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
result = [0] * (n + 1)

for num in range(1, n + 1):
    x, y, width, height = map(int, input().split())
    for i in range(x, x + width):
        for j in range(y, y + height):
            arr[i][j] = num

for num in range(1, n + 1):
    for lst in arr:
        result[num] += lst.count(num)

print(*result[1:], sep="\n")