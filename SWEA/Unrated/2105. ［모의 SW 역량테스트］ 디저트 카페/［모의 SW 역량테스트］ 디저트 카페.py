DIRECTIONS = [(1, 1), (-1, 1), (-1, -1), (1, -1)]  # 대각선 좌표


def dfs(row, col, rotate_cnt, visited):
    global max_dessert_cnt, start_row, start_col

    if row == start_row and col == start_col and rotate_cnt == 3:  # 원래 카페에 왔고, 3번 돌았다면, 갱신
        max_dessert_cnt = max(max_dessert_cnt, len(visited))
        return

    if 0 <= row < N and 0 <= col < N and cafes[row][col] not in visited:
        visited.add(cafes[row][col])  # 카페 탐색했다

        next_row, next_col = row + DIRECTIONS[rotate_cnt][0], col + DIRECTIONS[rotate_cnt][1]  # 직진 탐색
        dfs(next_row, next_col, rotate_cnt, visited)

        if rotate_cnt < 3:
            rotate_cnt += 1
            next_row, next_col = row + DIRECTIONS[rotate_cnt][0], col + DIRECTIONS[rotate_cnt][1]  # 대각선 탐색
            dfs(next_row, next_col, rotate_cnt, visited)

        visited.remove(cafes[row][col])  # 카페 탐색 안했다

T = int(input())
for testcase in range(1, T+1):
    N = int(input())  # 행렬 크기
    cafes = [list(map(int, input().split())) for _ in range(N)]

    max_dessert_cnt = -1

    for start_row in range(N):
        for start_col in range(N):
            dfs(start_row, start_col, 0, set())

    print(f'#{testcase} {max_dessert_cnt}')
