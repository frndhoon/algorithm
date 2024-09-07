BLACKHOLE = -1
def play_pinball_game(start_x, start_y, initial_direction):
    score = 0
    x, y = start_x, start_y

    while True:
        # 현재 방향으로 이동
        next_x = x + DIRECTIONS[initial_direction][0]
        next_y = y + DIRECTIONS[initial_direction][1]

        if game_map[next_y][next_x] == BLACKHOLE:  # 블랙홀에 도착
            return score

        elif 1 <= game_map[next_y][next_x] <= 5:  # 블록에 도착
            score += 1
            initial_direction = DIRECTION_CHANGE[game_map[next_y][next_x]][initial_direction]
            x, y = next_x, next_y

        elif 6 <= game_map[next_y][next_x] <= 10:  # 웜홀에 도착
            # 웜홀의 다른 위치를 찾아 이동
            wormhole_list = wormholes[game_map[next_y][next_x]]
            for (hole_x, hole_y) in wormhole_list:
                if hole_x != next_x or hole_y != next_y:
                    x, y = hole_x, hole_y
                    break

        elif game_map[next_y][next_x] == 0:  # 빈 공간
            x, y = next_x, next_y

        # 원래 출발 위치로 돌아오면
        if x == start_x and y == start_y:
            return score


# 방향 델타: 위, 아래, 왼쪽, 오른쪽
DIRECTIONS = [[0, -1], [0, 1], [-1, 0], [1, 0]]

# 블록 1-5에 대한 방향 변경
DIRECTION_CHANGE = {
                    1: {0: 1, 1: 3, 2: 0, 3: 2},
                    2: {0: 3, 1: 0, 2: 1, 3: 2},
                    3: {0: 2, 1: 0, 2: 3, 3: 1},
                    4: {0: 1, 1: 2, 2: 3, 3: 0},
                    5: {0: 1, 1: 0, 2: 3, 3: 2}
                    }

# 입력 읽기
test_cases = int(input())

for case_number in range(1, test_cases + 1):
    n = int(input())

    # 벽으로 초기화된 보드 (값 5)
    game_map = [[5] * (n + 2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(n)] + [[5] * (n + 2)]

    # 웜홀 초기화
    wormholes = {6: [], 7: [], 8: [], 9: [], 10: []}

    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if 6 <= game_map[y][x] <= 10:
                wormholes[game_map[y][x]].append((x, y))

    # 최대 점수 계산
    max_score = 0

    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if game_map[y][x] == 0:  # 빈 공간에서 시작
                for direction in range(4):
                    next_x = x + DIRECTIONS[direction][0]
                    next_y = y + DIRECTIONS[direction][1]

                    if game_map[next_y][next_x] == 0 or game_map[next_y][next_x] == BLACKHOLE:  # 이동하는 방향이 비어있거나 블랙홀이면 다른 경우에서 중복됨
                        continue

                    score = play_pinball_game(x, y, direction)
                    max_score = max(max_score, score)

    print(f'#{case_number} {max_score}')
