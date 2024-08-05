T = int(input())

for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    
    # 1일 경우 dp 바로 dp[0][1]과 d[1][1]의 max 값 출력
    if n == 1:
        print(*max(dp))

    # 아닐 경우, 초기값 설정
    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for idx in range(2, n):
            dp[0][idx] += max(dp[1][idx - 1], dp[1][idx - 2])
            dp[1][idx] += max(dp[0][idx - 1], dp[0][idx - 2])

        print(max(dp[0][n - 1], dp[1][n - 1]))
