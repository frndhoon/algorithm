from collections import deque
MAX_SIZE = int(input())

matrix = [list(map(int, input())) for _ in range(MAX_SIZE)]
visited = set()


def bfs(start_r, start_c):
    """
    단지 수 세아리는 bfs 탐색
    :param start_r: 시작 지점(row)
    :param start_c: 시작 지점(col)
    :return: 단지 수
    """

    queue = deque([(start_r, start_c)])
    visited.add((start_r, start_c))
    apt_cnt = 0

    while queue:
        current_r, current_c = queue.popleft()
        apt_cnt += 1
        for dir_r, dir_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_r = current_r + dir_r
            next_c = current_c + dir_c
            if next_r < 0 or next_r >= MAX_SIZE or next_c < 0 or next_c >= MAX_SIZE:
                continue
            if (next_r, next_c) in visited:
                continue
            if matrix[next_r][next_c]:
                visited.add((next_r, next_c))
                queue.append((next_r, next_c))

    return apt_cnt


apt_cnt_list = []

for row in range(MAX_SIZE):
    for col in range(MAX_SIZE):
        if matrix[row][col] and (row, col) not in visited:
            apt_cnt_list.append(bfs(row, col))

apt_cnt_list.sort()
print(len(apt_cnt_list), *apt_cnt_list, sep='\n')
