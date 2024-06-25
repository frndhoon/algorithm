import sys
input = sys.stdin.readline

height = [int(input()) for _ in range(9)]
heightSum = sum(height)

one = 0
two = 0

for i in range(9):
    for j in range(i + 1, 9):
        liar = height[i] + height[j]
        if heightSum - liar == 100:
            one = height[i]
            two = height[j]

height.remove(one)
height.remove(two)
height.sort()

print(*height, sep="\n")
