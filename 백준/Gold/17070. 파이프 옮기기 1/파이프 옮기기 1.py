# 1초, 집 크기 최대 16x16
N = int(input())
END_X, END_Y = N - 1, N - 1  # N이 3일 때, 오른쪽 대각선 끝 좌표는 (2, 2)
WALL = 1
# n x n 격자
house = [list(map(int, input().split())) for _ in range(N)]

# 3차원 dp 행렬, 0 = right, 1 = down, 2 = diagonal
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

# 초기 상태 설정 (시작점에 벽이 있으면 불가능)
if house[0][1] != WALL:
    dp[0][1][0] = 1

for x in range(N):
    for y in range(N):
        if house[x][y] == WALL:
            continue

        # 가로
        if y > 0:
            dp[x][y][0] += dp[x][y-1][0] + dp[x][y-1][2]

        # 세로
        if x > 0:
            dp[x][y][1] += dp[x-1][y][1] + dp[x-1][y][2]

        # 대각선
        if x > 0 and y > 0 and house[x-1][y] != WALL and house[x][y-1] != WALL:
            dp[x][y][2] += dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]

# 방법 수: 1,000,000보다 작거나 같음
cnt = sum(dp[END_X][END_Y])

print(cnt)