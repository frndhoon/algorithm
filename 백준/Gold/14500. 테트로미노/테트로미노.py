height, width = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(height)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_score = 0


# t 모양 제외 탐색
def dfs(x, y):
    global max_score
    stack = [(x, y, [(x, y)], paper[x][y])]

    while stack:
        x, y, path, score = stack.pop()
        # 4개 경로 탐색했다면, max값 갱신
        if len(path) == 4:
            max_score = max(max_score, score)
        else:
            for dx, dy in dir:
                nx, ny = dx + x, dy + y
                if 0 <= nx < height and 0 <= ny < width and (nx, ny) not in path:
                    # 탐색 방향 저장
                    new_path = path + [(nx, ny)]
                    stack.append((nx, ny, new_path, score + paper[nx][ny]))


# t 모양 탐색
def t_pixel(x, y):
    global max_score

    for i in range(4):
        # x, y는 중앙값임
        score = paper[x][y]
        # 상하좌우 중 3방향으로만 움직이면 됨
        for j in range(3):
            nx, ny = x + dir[(i + j) % 4][0], y + dir[(i + j) % 4][1]
            if 0 <= nx < height and 0 <= ny < width:
                score += paper[nx][ny]

        # 3방향으로 다 움직였을 때, max값 갱신
        max_score = max(max_score, score)


for x in range(height):
    for y in range(width):
        dfs(x, y)
        t_pixel(x, y)

print(max_score)