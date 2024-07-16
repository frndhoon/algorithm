import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [[0] * 41 for _ in range(2)]
dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 41):
    dp[0][i] = dp[0][i - 1] + dp[0][i - 2]
    dp[1][i] = dp[1][i - 1] + dp[1][i - 2]

for _ in range(n):
    value = int(input().rstrip())
    print(dp[0][value], dp[1][value])

