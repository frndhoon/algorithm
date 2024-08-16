from collections import deque
import copy

# 1초, 최대 15x15
# 행의 수: N
# 열의 수: M
# 공격 거리 제한: D
N, M, D = map(int, input().split())
# 적은 1
ENEMY = 1

# N+1행에 궁수가 있음
castle = [list(map(int, input().split())) for _ in range(N)]

# 공격 범위
attack_range = [(0, -1), (-1, 0), (0, 1)]

# 최대 적 제거 수
max_death_enemy_cnt = 0


# 적이 남아있는지 체크
def bfs(archers):
    current_castle = copy.deepcopy(castle)
    already_attacked = [[False] * M for _ in range(N)]
    death_enemy_cnt = 0

    for i in range(N - 1, -1, -1):
        death_enemy_list = []
        for archer_col in archers:
            # 행, 열, 사정거리(1) 추가
            queue = deque([(i, archer_col, 1)])
            while queue:
                attack_row, attack_col, dist = queue.popleft()
                if current_castle[attack_row][attack_col] == ENEMY:
                    death_enemy_list.append((attack_row, attack_col))
                    if not already_attacked[attack_row][attack_col]:
                        already_attacked[attack_row][attack_col] = True
                        death_enemy_cnt += 1
                    break  # 적 찾으면 해당 궁수는 더 이상 탐색할 필요 없음

                # 사거리 미만이면 최대 사거리까지 탐색
                if dist < D:
                    for dx, dy in attack_range:
                        nx, ny = dx + attack_row, dy + attack_col
                        if 0 <= nx < N and 0 <= ny < M:
                            queue.append((nx, ny, dist + 1))

        # 죽은 것 0으로 표시
        for death_x, death_y in death_enemy_list:
            current_castle[death_x][death_y] = 0

    return death_enemy_cnt


# 궁수 순열 탐색
def set_archers(lst, idx=0):
    global max_death_enemy_cnt
    if len(lst) == 3:
        max_death_enemy_cnt = max(max_death_enemy_cnt, bfs(lst))
        return

    for i in range(idx, M):
        lst.append(i)
        set_archers(lst, i + 1)
        lst.pop()


set_archers([])
print(max_death_enemy_cnt)
