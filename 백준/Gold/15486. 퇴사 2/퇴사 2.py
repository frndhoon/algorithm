days = int(input())
dp = [0] * (days + 1)

for day in range(1, days+1):
    period, cost = map(int, input().split())

    # 현재 날짜 상담을 선택하지 않는 경우
    dp[day] = max(dp[day], dp[day-1])

    # 현재 날짜 상담을 선택하는 경우
    if day + period - 1 <= days:
        dp[day+period-1] = max(dp[day+period-1], dp[day-1] + cost)

print(dp[-1])