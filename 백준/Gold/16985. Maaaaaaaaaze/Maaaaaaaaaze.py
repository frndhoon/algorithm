import pprint
from collections import deque

print = pprint.pprint


# [1] 판 회전시키기
def rotate_board(board):
    rotations = [board]
    for _ in range(3):
        board = list(map(list, zip(*board[::-1])))
        rotations.append(board)
    return rotations


min_move = float('inf')


# [2] 판 5개면 탈출시키기 (모든 가능한 조합을 확인)
def generate_combinations(current_maze, depth):
    global min_move
    if depth == 5:
        move = bfs(current_maze)
        if move != -1:
            min_move = min(min_move, move)
        return

    for i in range(5):
        if not used[i]:
            used[i] = True
            for rotation in rotations[i]:
                generate_combinations(current_maze + [rotation], depth + 1)
            used[i] = False

# [3] 출발, 탈출구가 있는지 확인
def check_start_end(maze_list):
    if maze_list[0][0][0] == 0 or maze_list[4][4][4] == 0:
        return None, None
    return (0, 0, 0), (4, 4, 4)


# [4] 탈출 시뮬레이션
def bfs(maze):
    start, end = check_start_end(maze)
    if start is None or end is None:
        return -1

    queue = deque([(start[0], start[1], start[2], 0)])  # (x, y, z, moves)
    visited = [[[float('inf')] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0

    directions = [
        (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)
    ]

    while queue:
        x, y, z, moves = queue.popleft()

        if (x, y, z) == end:
            return moves

        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and maze[nz][ny][nx] == 1 and visited[nz][ny][
                nx] > moves + 1:
                visited[nz][ny][nx] = moves + 1
                queue.append((nx, ny, nz, moves + 1))

    return -1


board_list = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
rotations = [rotate_board(board) for board in board_list]
used = [False] * 5

generate_combinations([], 0)
print(min_move if min_move != float('inf') else -1)