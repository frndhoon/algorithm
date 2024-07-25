width, height = list(map(int, input().split()))
boxes = [input().split() for _ in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def get_ripen_tomato_min_day(ripen_tomato_list):
    if not any('0' in row for row in boxes):
        return 0

    # 초기 queue는 익은 토마토 리스트 index 값 모음
    queue = ripen_tomato_list

    min_day = -1

    while queue:
        next_queue = []
        for current_x, current_y in queue:
            for x, y in zip(dx, dy):
                nx, ny = current_x + x, current_y + y
                if (0 <= nx < height and 0 <= ny < width) and not visited[nx][ny] and not boxes[nx][ny] == '-1':
                    visited[nx][ny] = True
                    boxes[nx][ny] = '1'
                    next_queue.append((nx, ny))
        # 상하좌우 안 익었은 토마토를 다 탐색해서 익게 했을 때,
        queue = next_queue
        min_day += 1

    return min_day


ripen_tomato = []
for x in range(len(boxes)):
    for y in range(len(boxes[x])):
        if boxes[x][y] == '1':
            ripen_tomato.append((x, y))

min_day = get_ripen_tomato_min_day(ripen_tomato)

if any('0' in row for row in boxes):
    print('-1')
else:
    print(min_day)
