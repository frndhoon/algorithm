def dfs(core_idx, connect_cnt, wire_len):
    """
    :param core_idx: 선택할 코어 인덱스
    :param connect_cnt: 코어에 전원 몇 개 연결됐는지 (갱신)
    :param wire_len: 전선 길이 합 (갱신)
    :return:
    """
    global max_connect_cnt, min_wire_len_sum

    if core_idx == len(core_list):
        # 최대 많은 코어에 전원에 연결하였을 경우,
        if connect_cnt > max_connect_cnt\
                or (connect_cnt == max_connect_cnt and wire_len < min_wire_len_sum):
                # 여러 방법이 있을 때, 전선 길이 합이 최소인 경우를 구해라
            max_connect_cnt = connect_cnt
            min_wire_len_sum = wire_len
        return

    cy, cx = core_list[core_idx]

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = cy + dy, cx + dx
        tmp_connect_pos_list = []

        while 0 <= ny < N and 0 <= nx < N and maxinoff[ny][nx] == 0:
            tmp_connect_pos_list.append((ny, nx))
            ny, nx = ny + dy, nx + dx
        
        # 전선 끝까지 연결됐을 때만,
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            # 전선 연결
            for ty, tx in tmp_connect_pos_list:
                maxinoff[ty][tx] = -1

            dfs(core_idx + 1, connect_cnt + 1, wire_len + len(tmp_connect_pos_list))

            # 원상복구
            for ty, tx in tmp_connect_pos_list:
                maxinoff[ty][tx] = 0

    # 연결 안되더라도 다음 전선으로 가기
    dfs(core_idx + 1, connect_cnt, wire_len)


T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    maxinoff = [list(map(int, input().split())) for _ in range(N)]
    min_wire_len_sum = float('INF')  # 전선 길이 합이 최소인지
    max_connect_cnt = 0  # 최대한 많은 core에 전원을 연결했는지
    core_list = []

    # 가장자리는 볼 필요 없음
    for row in range(1, N - 1):
        for col in range(1, N - 1):
            if maxinoff[row][col] == 1:
                core_list.append((row, col))

    dfs(0, 0, 0)
    print(f'#{testcase} {min_wire_len_sum}')
