from collections import deque
# 0.5초 2 <= N <= 10
N = int(input())
POPULATION = list(map(int, input().split()))
zone = [[] for _ in range(N)]
min_diff = 999

for n in range(N):
    info = list(map(int, input().split()))
    for i in range(1, len(info)):
        zone[n].append(info[i] - 1)


# 서로 연결돼있는지 탐색
def is_connected(group):
    if not group:
        return False
    q = deque([group[0]])
    visited = [False] * N
    visited[group[0]] = True
    cnt = 1

    while q:
        current = q.popleft()
        for neighbor in zone[current]:
            if neighbor in group and not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                cnt += 1

    return cnt == len(group)


# 그룹 내 인구 수 구하기
def get_population(group):
    population = 0
    for g in group:
        population += POPULATION[g]

    return population


def solve(index, red_zone):
    global min_diff

    if index == N:
        blue_zone = [i for i in range(N) if i not in red_zone]
        if red_zone and blue_zone:
            if is_connected(red_zone) and is_connected(blue_zone):
                diff = abs(get_population(red_zone) - get_population(blue_zone))
                min_diff = min(min_diff, diff)
        return

    # 현재 구역을 red_zone에 추가하지 않는 경우
    solve(index + 1, red_zone)

    # 현재 구역을 red_zone에 추가하는 경우
    solve(index + 1, red_zone + [index])


solve(0, [])

print(min_diff if min_diff != 999 else -1)
