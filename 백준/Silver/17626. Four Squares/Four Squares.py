import sys
input = sys.stdin.readline

n = int(input())

dp = [0, 1]

# 2부터 돌기
for idx in range(2, n + 1):
    min_val = 4
    
    # 제곱수
    for i in range(1, int(idx**0.5) + 1):
        min_val = min(min_val, dp[idx - (i ** 2)])

    dp.append(min_val + 1)

print(dp[n])