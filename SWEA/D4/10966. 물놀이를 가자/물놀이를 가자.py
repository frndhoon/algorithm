from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

def bfs():
    queue = deque()
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 'W':  # 물일 때부터 탐색 시작
                queue.append((r, c))
                distance[r][c] = 0

    while queue:
        cr, cc = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < row and 0 <= nc < col and distance[nr][nc] == -1:
                if matrix[nr][nc] == 'L':
                    distance[nr][nc] = distance[cr][cc] + 1
                    queue.append((nr, nc))


T = int(input())
for testcase in range(1, T+1):
    row, col = map(int, input().split())
    matrix = [input() for _ in range(row)]
    distance = [[-1] * col for _ in range(row)]
    
    bfs()
    
    total_distance = 0
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 'L':
                total_distance += distance[r][c]

    print(f'#{testcase} {total_distance}')
