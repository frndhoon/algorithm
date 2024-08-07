from collections import deque
width, depth, height = map(int, input().split())

# 위아래상하좌우
dir = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]

boxes_matrix = []
visited = []
isAllRipen = True

for _ in range(height):
    boxes_matrix.append([list(map(int, input().split())) for _ in range(depth)])
    visited.append([[False] * width for _ in range(depth)])

# 초기에 하나라도 안 익은게 있는지 체크
for boxes in boxes_matrix:
    for box in boxes:
        if 0 in box:
            isAllRipen = False
            break


def bfs(init_coordinate):
    queue = deque(init_coordinate)
    while queue:
        current_h, current_x, current_y = queue.popleft()
        day = boxes_matrix[current_h][current_x][current_y]
        for dh, dx, dy in dir:
            nh, nx, ny = current_h + dh, current_x + dx, current_y + dy
            if 0 <= nh < height and 0 <= nx < depth and 0 <= ny < width and boxes_matrix[nh][nx][ny] == 0:
                visited[nh][nx][ny] = True
                boxes_matrix[nh][nx][ny] = boxes_matrix[current_h][current_x][current_y] + 1
                queue.append((nh, nx, ny))


# 초기 익은 토마토 좌표값
init_coordinate = []

for h in range(height):
    for x in range(depth):
        for y in range(width):
            if boxes_matrix[h][x][y] == 1 and not visited[h][x][y]:
                visited[h][x][y] = True
                init_coordinate.append((h, x, y))


bfs(init_coordinate)

ripen_day = -1

for boxes in boxes_matrix:
    for box in boxes:
        # 하나라도 안 익은 게 있다면, 실패(-1)
        if 0 in box:
            print(-1)
            exit()
        # 아니라면 갱신
        else:
            ripen_day = max(ripen_day, max(box) - 1)

if isAllRipen:
    print(0)
else:
    print(ripen_day)
