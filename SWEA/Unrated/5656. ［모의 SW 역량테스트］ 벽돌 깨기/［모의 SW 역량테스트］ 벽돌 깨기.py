import copy
T = int(input())
DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 매트릭스 내리기
def down_matrix(matrix):
    new_matrix = [[0] * W for _ in range(H)]
    for w in range(W):
        current_h = H - 1
        for h in range(H - 1, -1, -1):
            if matrix[h][w]:
                new_matrix[current_h][w] = matrix[h][w]
                current_h -= 1
    return new_matrix


# 벽돌 부수기
def explore_brick(matrix, x, y, power):
    stack = [(x, y, power)]
    while stack:
        cx, cy, cp = stack.pop()
        matrix[cx][cy] = 0
        if cp > 1:
            for dx, dy in DELTAS:
                for i in range(1, cp):
                    nx, ny = cx + dx * i, cy + dy * i
                    if 0 <= nx < H and 0 <= ny < W and matrix[nx][ny] != 0:
                        stack.append((nx, ny, matrix[nx][ny]))
                        matrix[nx][ny] = 0

# 남은 벽돌 수 세기
def get_remain_brick(matrix):
    global min_cnt
    cnt = 0
    for x in range(H):
        for y in range(W):
            if matrix[x][y] != 0:
                cnt += 1
    min_cnt = min(min_cnt, cnt)


def brick_game(matrix, bead):
    # 구슬이 다 떨어졌으면 갱신
    if bead == 0:
        get_remain_brick(matrix)
        return

    for w in range(W):
        new_matrix = [row[:] for row in matrix]
        h = 0
        while h < H and new_matrix[h][w] == 0:
            h += 1
        if h == H:
            continue

        explore_brick(new_matrix, h, w, new_matrix[h][w])
        new_matrix = down_matrix(new_matrix)
        brick_game(new_matrix, bead - 1)


for testcase in range(1, T + 1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    min_cnt = float('inf')
    brick_game(matrix, N)
    print(f"#{testcase} {min_cnt if min_cnt != float('inf') else 0}")  # 벽돌 개수 갱신이 하나도 되지 않았을 때
