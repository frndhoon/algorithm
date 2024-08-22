from collections import deque
# 15초, 50 * 50, L <= 20
# [1] 맨홀 뚜껑 터널 (x좌표, y좌표, 맨홀 종류)
# [2] 터널 bfs 탐색(하나씩)
# [3] 맨홀 종류에 따라 탐색
# [4] 방문된 구역 개수 출력
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
TYPES = { # 맨홀뚜껑 종류
    1: (0, 1, 2, 3),
    2: (0, 1),
    3: (2, 3),
    4: (0, 3),
    5: (1, 3),
    6: (1, 2),
    7: (0, 2)
}
# 탐색 시 터널끼리 연결되는지 여부
# 상->하 / 하->상 / 좌->우 / 우->좌
CONNECTS = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}


T = int(input())

for testcase in range(1, T+1):
    # N * M, manhole = (R, C), 탈출 후 소요 시간 = L
    N, M, R, C, L = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # [1] 맨홀 뚜껑 터널 (x좌표, y좌표, 맨홀 종류)
    manhole = (R, C, matrix[R][C])
    visited = set()
    visited.add((R, C))  # 맨홀 뚜껑 밑 터널은 방문 처리

    queue = deque([manhole])

    # [2] 터널 bfs 탐색(하나씩)
    for _ in range(L-1):
        temp = []
        while queue:
            cx, cy, c_type = queue.popleft()  # ex) (2, 1, 3)
            # [3] 맨홀 종류에 따라 탐색
            for t in TYPES[c_type]:
                dx, dy = DIRS[t]
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < N and 0 <= ny < M and matrix[nx][ny] != 0 and (nx, ny) not in visited and
                        CONNECTS[t] in TYPES[matrix[nx][ny]]):  # 탐색 시 터널끼리 연결되는지?
                    visited.add((nx, ny))
                    temp.append((nx, ny, matrix[nx][ny]))
        queue = deque(temp)

    # [4] 방문된 구역 개수 출력
    print(f'#{testcase} {len(visited)}')
