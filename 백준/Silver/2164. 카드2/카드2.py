from collections import deque
n = int(input())

card_deck = deque(card for card in range(1, n + 1))

while len(card_deck) > 1:
    card_deck.popleft()
    card_deck.append(card_deck.popleft())

print(card_deck[0])