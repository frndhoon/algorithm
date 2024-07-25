from collections import deque

width, height = list(map(int, input().split()))
boxes = [input().split() for _ in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def get_ripen_tomato_min_day():

    # 이미 모든 토마토가 익었는가 체크
    already_ripe_found = False
    for row in boxes:
        if '0' in row:
            already_ripe_found = True
            break
    # 이미 모든 토마토가 다 익었다면 0 출력
    if not already_ripe_found:
        return 0

    queue = deque()
    # 초기 queue는 익은 토마토 리스트
    for x in range(len(boxes)):
        for y in range(len(boxes[x])):
            if boxes[x][y] == '1':
                queue.append((x, y))
                visited[x][y] = True

    min_day = 0

    while queue:
        # 기존에 있던 queue length만큼 popleft()
        for _ in range(len(queue)):
            current_x, current_y = queue.popleft()
            for x, y in zip(dx, dy):
                nx, ny = current_x + x, current_y + y
                if (0 <= nx < height and 0 <= ny < width) and not visited[nx][ny] and not boxes[nx][ny] == '-1':
                    visited[nx][ny] = True
                    boxes[nx][ny] = '1'
                    queue.append((nx, ny))
        # 안 익은 토마토를 상하좌우 탐색해서 익게 했을 때,
        min_day += 1

    # 큐가 비었을 때 마지막으로 하루가 증가함
    return min_day - 1


min_day = get_ripen_tomato_min_day()

# 토마토가 모두 익지 못하는 상황 체크
is_unripe = False
for row in boxes:
    if '0' in row:
        is_unripe = True
        break


# 토마토가 모두 익지 못했다면 -1
if is_unripe:
    print('-1')
else:
    print(min_day)
