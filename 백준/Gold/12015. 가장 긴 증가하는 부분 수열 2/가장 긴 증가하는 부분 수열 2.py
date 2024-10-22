N = int(input())

arr = list(map(int, input().split()))

dp = [arr[0]]

for num in arr:
    if dp[-1] < num:  # 다음 원소가 현재 최댓값보다 크다면 넣어주기
        dp.append(num)
    else:  # 아니라면, 중간에 갱신해야할 값 찾기 (이분탐색)
        start = 0
        end = len(dp)-1
        while start <= end:
            mid = (start+end)//2

            if dp[mid] < num:
                start = mid + 1
            else:
                end = mid - 1
        dp[start] = num

print(len(dp))