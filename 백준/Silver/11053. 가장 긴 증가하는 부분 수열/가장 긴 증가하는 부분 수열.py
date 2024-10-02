arr_len = int(input())
arr = list(map(int, input().split()))

dp = [1] * arr_len

for idx in range(1, arr_len):

    target_idx = idx

    while idx > 0:
        if arr[target_idx] > arr[idx-1]:  # 증가하는 수열이라면
            dp[target_idx] = max(dp[target_idx], dp[idx-1] + 1)  # 최대 부분 수열 길이 갱신하기
        idx -= 1


print(max(dp))
