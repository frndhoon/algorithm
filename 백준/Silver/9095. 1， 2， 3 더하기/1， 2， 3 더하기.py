from collections import defaultdict
testcase = int(input())
for _ in range(testcase):
    
    num = int(input())
    
    dp = defaultdict(list)
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if num >= 4:
        for n in range(4, num+1):
            dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

    print(dp[num])
