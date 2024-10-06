from collections import deque

GROUND_MOVE = 'G'
TREE_CANT_MOVE = 'T'
START_LOCATION = 'X'
ARRIVE_LOCATION = 'Y'

T = int(input())


def get_point(point):
    """
    해당 지점 행, 열 값 찾기
    :param point: 스타트 지점인지, 도착 지점인지
    :return: 지점 열, 지점 행
    """
    for col in range(N):
        for row in range(N):
            if matrix[col][row] == point:
                return col, row


for testcase in range(1, T + 1):
    N, cut_cnt = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    start_col, start_row = get_point(START_LOCATION)

    # 4차원 배열로 distances 생성 (col, row, 방향, 남은 cut_cnt)
    distances = [[[[float('inf')] * (cut_cnt + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    distances[start_col][start_row][0][cut_cnt] = 0  # 시작점에서의 리모컨 조작 횟수는 0, 방향은 'up'

    def bfs(start_col, start_row, cut_cnt):
        """
        bfs 탐색
        :param start_col: 시작 지점(행)
        :param start_row: 시작 지점(열)
        :param cut_cnt: 최대 나무 베기 개수
        :return:
        """
        # 열, 행, 방향, 남은 cut_cnt, 리모컨 조작 횟수
        queue = deque([(start_col, start_row, 0, cut_cnt, 0)])

        # 상, 우, 하, 좌 방향
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            current_col, current_row, current_view, remaining_cut_cnt, remote_cnt = queue.popleft()

            # 도착 했으면 탐색 종료
            if matrix[current_col][current_row] == ARRIVE_LOCATION: continue

            # 현재 방향으로 앞으로 이동 시도
            next_col = current_col + DIRECTIONS[current_view][0]
            next_row = current_row + DIRECTIONS[current_view][1]

            if 0 <= next_col < N and 0 <= next_row < N:
                # GROUND_MOVE 또는 ARRIVE_LOCATION으로 이동할 때
                if matrix[next_col][next_row] == GROUND_MOVE or matrix[next_col][next_row] == ARRIVE_LOCATION:
                    if distances[next_col][next_row][current_view][remaining_cut_cnt] > remote_cnt + 1:
                        distances[next_col][next_row][current_view][remaining_cut_cnt] = remote_cnt + 1
                        queue.append((next_col, next_row, current_view, remaining_cut_cnt, remote_cnt + 1))

                # TREE_CANT_MOVE로 이동하려면 나무를 베어야 함
                elif matrix[next_col][next_row] == TREE_CANT_MOVE and remaining_cut_cnt > 0:
                    if distances[next_col][next_row][current_view][remaining_cut_cnt - 1] > remote_cnt + 1:
                        distances[next_col][next_row][current_view][remaining_cut_cnt - 1] = remote_cnt + 1
                        queue.append((next_col, next_row, current_view, remaining_cut_cnt - 1, remote_cnt + 1))

            # 좌우 회전 (방향만 바뀌고 이동은 하지 않음)
            new_views = [(current_view - 1) % 4, (current_view + 1) % 4]  # 좌회전, 우회전
            for new_view in new_views:
                if distances[current_col][current_row][new_view][remaining_cut_cnt] > remote_cnt + 1:
                    distances[current_col][current_row][new_view][remaining_cut_cnt] = remote_cnt + 1
                    queue.append((current_col, current_row, new_view, remaining_cut_cnt, remote_cnt + 1))


    bfs(start_col, start_row, cut_cnt)

    # 도착지점의 최소 리모컨 조작 횟수 확인
    arrive_col, arrive_row = get_point(ARRIVE_LOCATION)

    result = float('inf')
    for direction in range(4):  # 남은 cut_cnt에 상관없이 모든 방향에서의 최소 리모컨 조작 횟수 확인
        result = min(result, min(distances[arrive_col][arrive_row][direction]))

    if result == float('inf'):
        print(f"#{testcase} -1")  # 도착할 수 없을 때
    else:
        print(f"#{testcase} {result}")
