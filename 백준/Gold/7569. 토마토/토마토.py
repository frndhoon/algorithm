from collections import deque
width, depth, height = map(int, input().split())

# 위아래상하좌우
dir = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]

boxes_matrix = []
visited = []
isInitAllRipen = True

for _ in range(height):
    boxes_matrix.append([list(map(int, input().split())) for _ in range(depth)])
    visited.append([[False] * width for _ in range(depth)])

# 초기에 하나라도 안 익은게 있는지 체크
for boxes in boxes_matrix:
    for box in boxes:
        if 0 in box:
            isInitAllRipen = False
            break
    if not isInitAllRipen:
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
                boxes_matrix[nh][nx][ny] = day + 1
                queue.append((nh, nx, ny))


# 초기 익은 토마토 좌표값
init_coordinate = []

for h in range(height):
    for x in range(depth):
        for y in range(width):
            if boxes_matrix[h][x][y] == 1 and not visited[h][x][y]:
                visited[h][x][y] = True
                init_coordinate.append((h, x, y))


def getRipenday(isInitAllRipen, init_coordinate):
    
    # 초기에 다 안 익었을 때만, bfs 돌아라
    if not isInitAllRipen:
        bfs(init_coordinate)

        ripen_day = 0
        for boxes in boxes_matrix:
            for box in boxes:
                if 0 in box:
                    return - 1
                ripen_day = max(ripen_day, max(box) - 1)

    else:
        return 0

    return ripen_day

print(getRipenday(isInitAllRipen, init_coordinate))
