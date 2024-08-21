# N * M (최대 8 * 8)
# 사각지대 최소 크기
# [1] 회전 정보 저장 (x좌표, y좌표, 종류)
# [2] dfs로 회전 종류에 맞게 하나씩 탐색하면서 맵 변경
# [3] dfs를 CCTV 개수만큼 탐색한다면 종료
# [4] 0인 부분 개수 세고 최솟값 비교
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

WALL = 6

MODE = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [2, 1], [1, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [0, 1, 3]],
    5: [[0, 1, 2, 3]]
}

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
min_value = 1e6

cctv = []

# [1] 회전 정보 저장(x좌표, y좌표, 종류)
for x in range(N):
    for y in range(M):
        if matrix[x][y] in (1, 2, 3, 4, 5):
            cctv.append((x, y, matrix[x][y]))


# [2] dfs로 회전 종류에 맞게 하나씩 탐색하면서 맵 변경
def search(x, y, dirs, matrix):
    for d in dirs:  # dir = [0] ~ [0, 1, 2, 3]
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            dx, dy = DIRS[d]
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] != WALL:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = '#'
                stack.append((nx, ny))


# [3] dfs를 CCTV 개수만큼 탐색한다면 종료
def dfs(cnt, matrix):
    global min_value
    if cnt == len(cctv):
        min_value = min(min_value, get_four_dimension(matrix))
        return

    temp = [row[:] for row in matrix]  # 임시 값 저장

    x, y, mode = cctv[cnt]  # ex) (2, 2, 1)
    for dirs in MODE[mode]:  # MODE[1] = [[0], [1], [2], [3]]
        search(x, y, dirs, temp)
        dfs(cnt + 1, temp)
        temp = [row[:] for row in matrix]  # for문 다 돌았으면 바로 전 걸로 다시 저장


# [4] 0인 부분 개수 세고 최솟값 비교
def get_four_dimension(matrix):
    four_dimension = 0
    for x in range(N):
        for y in range(M):
            if matrix[x][y] == 0:
                four_dimension += 1

    return four_dimension


dfs(0, matrix)

print(min_value)
