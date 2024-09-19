# 치킨 배달
N, M = map(int, input().split())

chicks = []

homes = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            homes.append((i, j))
        elif row[j] == 2:
            chicks.append((i, j))

visited = [False] * len(chicks)

min_dist = 1e9


def get_chicken_distance():
    entire_distance = 0

    for i in homes:  # 집 좌표에 대해 모든 치킨집과의 거리를 구함
        distance = 1e9
        for j in range(len(visited)):
            if visited[j]:
                check_num = abs(i[0] - chicks[j][0]) + abs(i[1] - chicks[j][1])
                distance = min(distance, check_num)  # 각 집에 대해 치킨 거리가 최소인 값을 구함

        entire_distance += distance

    return entire_distance


def dfs(idx=0, cnt=0):
    """
    :param idx: visited 인덱스
    :param cnt: 치킨집 개수
    :return:
    """

    global min_dist

    if cnt == M:
        dist = get_chicken_distance()
        min_dist = min(dist, min_dist)

        return

    for i in range(idx, len(chicks)):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False


dfs()

print(min_dist)
