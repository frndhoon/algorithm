n = int(input())
dp = [0, 0, 1, 1]

for idx in range(4, n + 1):
    if idx % 2 == 0 and idx % 3 == 0:
        dp.append(min(dp[idx // 2] + 1, dp[idx // 3] + 1, dp[idx - 1] + 1))
    elif idx % 3 == 0:
        dp.append(min(dp[idx // 3] + 1, dp[idx - 1] + 1))
    elif idx % 2 == 0:
        dp.append(min(dp[idx // 2] + 1, dp[idx - 1] + 1))
    else:
        idx = idx - 1
        if idx % 2 == 0 and idx % 3 == 0:
            dp.append(min(dp[idx // 2] + 2, dp[idx // 3] + 2, dp[idx - 1] + 2))
        elif idx % 3 == 0:
            dp.append(min(dp[idx // 3] + 2, dp[idx - 1] + 2))
        elif idx % 2 == 0:
            dp.append(min(dp[idx // 2] + 2, dp[idx - 1] + 2))

print(dp[n])