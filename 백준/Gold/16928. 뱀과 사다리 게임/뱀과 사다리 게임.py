from collections import defaultdict, deque

ladder_cnt, snake_cnt = map(int, input().split())

board = {}

for _ in range(ladder_cnt):
    st, ed = map(int, input().split())
    board[st] = ed

for _ in range(snake_cnt):
    st, ed = map(int, input().split())
    board[st] = ed


def bfs():
    """
    bfs 탐색
    :return: 도착했을 때 주사위 던진 횟수
    """
    queue = deque([(1, 0)])  # (position, moves)
    visited = set()

    while queue:
        pos, moves = queue.popleft()

        if pos == 100:
            return moves

        for dice in range(1, 7):
            next_pos = pos + dice

            if next_pos > 100:
                continue

            if next_pos in board:
                next_pos = board[next_pos]

            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, moves + 1))

print(bfs())