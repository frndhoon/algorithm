arr_len = int(input())
arr = list(map(int, input().split()))

dp_asc = [1] * arr_len  # 증가
dp_desc = [1] * arr_len  # 거꾸로 증가

# 증가되는 수열
for idx in range(1, arr_len):
    target_idx = idx
    while idx > 0:
        if arr[target_idx] > arr[idx-1]:
            dp_asc[target_idx] = max(dp_asc[target_idx], dp_asc[idx-1]+1)

        idx -= 1

# 거꾸로 증가되는 수열
for idx in range(arr_len-2, -1, -1):
    target_idx = idx
    while idx < arr_len - 1:
        if arr[target_idx] > arr[idx+1]:
            dp_desc[target_idx] = max(dp_desc[target_idx], dp_desc[idx+1]+1)

        idx += 1

# 가장 긴 바이토닉 수열 길이 저장
dp = [1] * arr_len
for idx in range(arr_len):
    target_idx = idx
    while idx < arr_len - 1:
        if arr[target_idx] > arr[idx+1]:  # 현재 수열 값이 다음 수열 값보다 클 경우(Sk > Sk+1 > ... SN-1 > SN)
            # 자신의 최장 증가 수열 길이와 다음 값의 최장 감소 수열을 더하기
            dp[target_idx] = max(dp[target_idx], dp_asc[target_idx] + dp_desc[idx+1])

        idx += 1

print(max(dp))