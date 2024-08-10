import copy

depth, width = map(int, input().split())
init_lab = [list(map(int, input().split())) for _ in range(depth)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_safety_zone = 0


# 벽 3개 세웠다면, 바이러스 유출을 시키는 역할
def build_wall_and_laek_virus(lab_matrix, wall_cnt=0, start_x=0, start_y=0):

    if wall_cnt == 3:
        wall_lab_matrix = copy.deepcopy(lab_matrix)
        dfs(wall_lab_matrix, virus_point)
        return

    for x in range(start_x, depth):
        for y in range(start_y if x == start_x else 0, width):
            if lab_matrix[x][y] == 0:
                lab_matrix[x][y] = 1
                build_wall_and_laek_virus(lab_matrix, wall_cnt + 1, x, y)
                lab_matrix[x][y] = 0


# 여러 개의 바이러스 지점을 탐색하는 역할
def get_virus_point(lab_matrix):
    virus_point = []

    for x in range(depth):
        for y in range(width):
            if lab_matrix[x][y] == 2:
                virus_point.append((x, y))

    return virus_point


# 바이러스 지점 탐색
virus_point = get_virus_point(init_lab)


# 최대 안전 구역 갱신하는 역할
def get_max_safety_zone(lab_matrix):
    global max_safety_zone
    safety_zone = 0

    for x in range(depth):
        for y in range(width):
            if lab_matrix[x][y] == 0:
                safety_zone += 1

    if safety_zone > max_safety_zone:
        max_safety_zone = safety_zone


# dfs로 바이러스 감염시키는 역할
def dfs(lab_matrix, virus_point):
    stack = list(virus_point)
    while stack:
        current_x, current_y = stack.pop()
        for dx, dy in direct:
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < depth and 0 <= ny < width and lab_matrix[nx][ny] == 0:
                lab_matrix[nx][ny] = 2
                stack.append((nx, ny))

    # 바이러스 감염 시키고, 최대 안전 구역을 갱신함
    get_max_safety_zone(lab_matrix)


# 유출 시작
build_wall_and_laek_virus(init_lab)
# 최대 안전 구역을 출력
print(max_safety_zone)