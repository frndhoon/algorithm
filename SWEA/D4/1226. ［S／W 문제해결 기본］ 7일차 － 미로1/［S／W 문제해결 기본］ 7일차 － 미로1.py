from collections import deque
 
T = 10
 
WALL = 1
START = 2
END = 3
SIZE = 16
DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
 
# 시작지점 찾기
def get_start_point():
    for x in range(SIZE):
        for y in range(SIZE):
            if maze[x][y] == START:
                return x, y
 
 
# bfs
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
 
    while queue:
        current_x, current_y = queue.popleft()
 
        if maze[current_x][current_y] == END:
            return True
 
        for dx, dy in DELTAS:
            nx, ny = current_x + dx, current_y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE and maze[nx][ny] != WALL and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return False
 
 
for _ in range(1, T+1):
    testcase = int(input())
    maze = [list(map(int, input())) for _ in range(SIZE)]
    visited = [[False] * SIZE for _ in range(SIZE)]
 
    start_x, start_y = get_start_point()
 
    is_arrived = bfs(start_x, start_y)
 
    # 도착되면 1 안되면 0
    result = 1 if is_arrived else 0
 
    print(f'#{testcase} {result}')