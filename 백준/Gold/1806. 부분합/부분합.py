list_len, target_sum = map(int, input().split())
lst = list(map(int, input().split()))

st, ed = 0, 0
min_len = float('inf')  # 최소 길이
current_sum = lst[st]

while st <= ed:
    if current_sum >= target_sum:  # 부분 합이 목표 합 이상이라면, 최소 배열 길이 갱신
        min_len = min(min_len, ed - st + 1)
        current_sum -= lst[st]
        st += 1
    elif current_sum < target_sum:
        ed += 1
        if ed >= list_len:  # 배열 길이보다 초과하면 끝
            break
        current_sum += lst[ed]

print(min_len if min_len != float('inf') else 0)
