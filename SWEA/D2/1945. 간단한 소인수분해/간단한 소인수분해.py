T = int(input())

for testcase in range(1, T+1):
    num = int(input())
    num_lst = [2, 3, 5, 7, 11]
    cnt_lst = [0, 0, 0, 0, 0]
    for i in range(5):
        while num % num_lst[i] == 0:
            cnt_lst[i] += 1
            num //= num_lst[i]

    print(f'#{testcase}', end=' ')
    print(*cnt_lst)
    