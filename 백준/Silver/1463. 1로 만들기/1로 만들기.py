n = int(input())
dp = [0] * (n + 1)
dp[1] = 0

for idx in range(2, n + 1):
    dp[idx] = dp[idx - 1] + 1

    if idx % 2 == 0:
        dp[idx] = min(dp[idx], dp[idx//2] + 1)
    if idx % 3 == 0:
        dp[idx] = min(dp[idx], dp[idx//3] + 1)

print(dp[n])