from collections import deque
T = int(input())
BLANK = '.'
WALL = '#'
START = '@'  # 지도에 하나밖에 없음
FIRE = '*'


def bfs():
    queue = deque([])

    for y, x in fires:
        queue.append((y, x, "fire"))
    for y, x in sanggun:
        queue.append((y, x, "sanggun"))

    visited = [[-1] * width for _ in range(height)]
    visited[sanggun[0][0]][sanggun[0][1]] = 0  # 상근이 현재 위치는 0으로

    while queue:
        current_y, current_x, status = queue.popleft()
        for dir_y, dir_x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current_y + dir_y, current_x + dir_x
            if status == 'fire':
                if next_y < 0 or next_y >= height or next_x < 0 or next_x >= width: continue
                if building[next_y][next_x] == BLANK or building[next_y][next_x] == START:
                    building[next_y][next_x] = FIRE
                    queue.append((next_y, next_x, "fire"))
            elif status == 'sanggun':
                if next_y < 0 or next_y >= height or next_x < 0 or next_x >= width:  # 탈출 성공했으면 +1
                    return visited[current_y][current_x] + 1

                if building[next_y][next_x] == FIRE: continue  # 불인 곳 못 감
                if building[next_y][next_x] == WALL: continue  # 벽인 곳 못 감

                if visited[next_y][next_x] == -1:  # 방문한 곳이 아닐 때만,
                    visited[next_y][next_x] = visited[current_y][current_x] + 1
                    queue.append((next_y, next_x, "sanggun"))

    return "IMPOSSIBLE"


for _ in range(T):
    width, height = map(int, input().split())
    building = [list(input()) for _ in range(height)]

    sanggun = []
    fires = []

    for y in range(height):
        for x in range(width):
            if building[y][x] == START:
                sanggun.append((y, x))
            elif building[y][x] == FIRE:
                fires.append((y, x))

    answer = bfs()
    print(answer)

