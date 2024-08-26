def divide_and_shuffle_cards(card_list):
    N = len(card_list)
    deck = [0] * N

    d = (N + 1) // 2  # 아래 카드 시작, N//2+N%2
    i1 = 0
    i2 = d
    i3 = 0  # 새로 만들 덱의 인덱스

    while i3 < N:
        if i1 < d:
            deck[i3] = card_list[i1]
            i1 += 1
            i3 += 1
        if i2 < N:
            deck[i3] = card_list[i2]
            i2 += 1
            i3 += 1

    return deck


T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    card_list = input().split()

    shuffled_deck = divide_and_shuffle_cards(card_list)
    print(f"#{testcase}", *shuffled_deck)