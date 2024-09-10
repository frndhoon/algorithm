from collections import deque
N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

def bfs(start_y, start_x):
    """
    bfs로 최단 경로, 시작하는 칸과 끝나는 칸도 포함해서 세기
    :param start_y: 시작 y
    :param start_x: 시작 x
    :return: 최단경로
    """
    queue = deque([(start_y, start_x, 0)])
    distance = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # 3차원 행렬로 벽 부순 경우, 안 부순 경우 나누기
    distance[start_y][start_x][0] = 1

    while queue:
        current_y, current_x, break_cnt = queue.popleft()

        if (current_y, current_x) == (N - 1, M - 1):
            return distance[current_y][current_x][break_cnt]

        for dir_y, dir_x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current_y + dir_y, current_x + dir_x

            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= M:
                continue

            # 벽인 경우 벽 부수기
            if matrix[next_y][next_x] == 1 and break_cnt == 0:
                distance[next_y][next_x][1] = distance[current_y][current_x][0] + 1
                queue.append([next_y, next_x, 1])

            # 이동 가능하며, 해당 break_cnt 층에서 아직 방문하지 않았다면,
            elif matrix[next_y][next_x] == 0 and distance[next_y][next_x][break_cnt] == 0:
                distance[next_y][next_x][break_cnt] = distance[current_y][current_x][break_cnt] + 1
                queue.append([next_y, next_x, break_cnt])

    return -1


print(bfs(0, 0))