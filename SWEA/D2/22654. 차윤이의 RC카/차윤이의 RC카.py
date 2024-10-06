GROUND_CAN_MOVE = 'G' # 이동 가능
TREE_CANT_MOVE = 'T' # 이동 불가
CURRENT_LOCATION = 'X'
ARRIVAL_LOCATION = 'Y'

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    cmd_cnt = int(input())

    # 상, 우, 하, 좌
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    up, right, down, left = 0, 1, 2, 3

    results = []

    for _ in range(cmd_cnt):
        cmd_len, commands = input().split()
        cmd_len = int(cmd_len)


        is_find = False
        for col in range(N):
            if is_find:
                break
            for row in range(N):
                if is_find:
                    break
                if matrix[col][row] == CURRENT_LOCATION:
                    current_col, current_row, current_view = col, row, up # 항상 위로 바라보는 방향으로부터 조종 시작

                    for command in commands:

                        # 앞으로 이동
                        if command == 'A':
                            current_col, current_row, current_view = (
                                current_col + DIRECTIONS[current_view][0], current_row + DIRECTIONS[current_view][1], current_view)
                            if matrix[current_col][current_row] == TREE_CANT_MOVE or current_row < 0 or current_row >= N or current_col < 0 or current_col >= N:
                                current_col, current_row, current_view = (
                                    current_col - DIRECTIONS[current_view][0],
                                    current_row - DIRECTIONS[current_view][1], current_view)
                        # 왼쪽으로 90도 회전
                        if command == 'L':
                            current_col, current_row, current_view = current_col, current_row, (current_view-1) % 4

                        # 오른쪽으로 90도 회전
                        if command == 'R':
                            current_col, current_row, current_view = current_col, current_row, (current_view+1) % 4
                    else:
                        if matrix[current_col][current_row] == ARRIVAL_LOCATION:
                            results.append(1) # 도달 가능
                        else:
                            results.append(0)
                        is_find = True
                        break
    print(f"#{testcase} {' '.join(map(str, results))}")