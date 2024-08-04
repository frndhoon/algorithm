T = int(input())
max_score = 101

for _ in range(T):
    cnt_lst = [0] * max_score
    testcase = input()
    num_lst = list(map(int, input().split()))

    for num in num_lst:
        cnt_lst[num] += 1

    max_idx = 0
    for idx in range(max_score):
        if cnt_lst[idx] >= cnt_lst[max_idx]:
            max_idx = idx

    print(f'#{testcase} {max_idx}')