T = int(input())

def get_balloon_cnt(x, y):
    global max_cnt
    balloon_cnt = matrix[x][y]
    
    for flower in range(1, matrix[x][y] + 1):
        for dx, dy in dir:
            # 안에 들어있는 꽃가루 수만큼 추가로 터짐
            nx, ny = x + dx * flower, y + dy * flower
            if 0 <= nx < n and 0 <= ny < m:
                balloon_cnt += matrix[nx][ny]

        if balloon_cnt > max_cnt:
            max_cnt = balloon_cnt

    return max_cnt

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
