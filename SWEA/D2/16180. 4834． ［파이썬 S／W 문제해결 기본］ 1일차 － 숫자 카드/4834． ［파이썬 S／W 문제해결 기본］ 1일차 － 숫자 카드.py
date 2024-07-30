T = int(input())


for testcase in range(1, T+1):
    card_num = int(input())
    cards = list(map(int, list(input())))
    max_val = cards[0]

    cnt_list = [0] * 10

    for card in cards:
        cnt_list[card] += 1

    max_card = 0
    max_cnt = cnt_list[0]
    for idx in range(10):
        if cnt_list[idx] >= max_cnt:
            max_card = idx
            max_cnt = cnt_list[idx]

    print(f'#{testcase} {max_card} {max_cnt}')
