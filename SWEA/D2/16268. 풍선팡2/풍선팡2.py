T = int(input())

def get_balloon_cnt(x, y):
    global max_cnt
    balloon_cnt = matrix[x][y]

    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        # 범위 안일 때 꽃가루 카운팅
        if 0 <= nx < n and 0 <= ny < m:
            balloon_cnt += matrix[nx][ny]

    if balloon_cnt > max_cnt:
        max_cnt = balloon_cnt


# 상하좌우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for testcase in range(1, T+1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0

    for x in range(n):
        for y in range(m):
            get_balloon_cnt(x, y)

    print(f'#{testcase} {max_cnt}')
