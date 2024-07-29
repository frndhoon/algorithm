from collections import deque
import copy

n = int(input())
normal_grid = [list(input()) for _ in range(n)]
RGB_grid = copy.deepcopy(normal_grid)
normal_visited = [[False for _ in range(n)] for _ in range(n)]
RGB_visited = copy.deepcopy(normal_visited)

# 적록색약으로 만들어주기
for x in range(n):
    for y in range(n):
        if RGB_grid[x][y] == 'G':
            RGB_grid[x][y] = 'R'
            
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 일반, 적록색약 cnt 따로 계산
normal_cnt = 0
RGB_cnt = 0


def get_color_area(x, y, grid, visited):
    target_color = grid[x][y]
    queue = deque([(x, y)])

    while queue:
        current_x, current_y = queue.popleft()
        for nx, ny in zip(dx, dy):
            exploreX = current_x + nx
            exploreY = current_y + ny
            if 0 <= exploreX < n and 0 <= exploreY < n and not visited[exploreX][exploreY] and grid[exploreX][exploreY] == target_color:
                queue.append((exploreX, exploreY))
                visited[exploreX][exploreY] = True


# 각각 계산해주기
for x in range(n):
    for y in range(n):
        if not normal_visited[x][y]:
            get_color_area(x, y, normal_grid, normal_visited)
            normal_cnt += 1

for x in range(n):
    for y in range(n):
        if not RGB_visited[x][y]:
            get_color_area(x, y, RGB_grid, RGB_visited)
            RGB_cnt += 1

print(normal_cnt, RGB_cnt)
