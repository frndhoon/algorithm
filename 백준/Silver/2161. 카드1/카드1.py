from collections import deque

num = int(input())
card_list = deque(i for i in range(1, num+1))

while len(card_list) != 1:
    print(card_list.popleft(), end=' ')
    card_list.append(card_list.popleft())

print(card_list[0])
