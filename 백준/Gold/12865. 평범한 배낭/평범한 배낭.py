cnt, endure = map(int, input().split())
dp = [0] * (endure + 1)

for _ in range(cnt):
    weight, value = map(int, input().split())
    for i in range(endure, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[endure])

