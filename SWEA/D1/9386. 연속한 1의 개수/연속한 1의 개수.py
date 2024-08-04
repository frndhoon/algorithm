T = int(input())

for testcase in range(1, T+1):
    length = int(input())
    num_list = list(map(int, input()))

    current_cnt = 0
    max_cnt = 0

    for idx in range(length):
        if num_list[idx] == 1:
            current_cnt += 1
            if current_cnt > max_cnt:
                max_cnt = current_cnt
        else:
            current_cnt = 0

    print(f'#{testcase} {max_cnt}')
