import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
num = list(map(int, input().split()))

maxSum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            numSum = num[i] + num[j] + num[k]
            if numSum > m:
                continue
            elif numSum <= m:
                maxSum = max(maxSum, numSum)

print(maxSum)