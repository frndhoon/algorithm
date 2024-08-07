T = 10
road_size = 101
start_city = 0
end_city = 99


def dfs(start, end):
    stack = [start]
    visited[start] = True

    while stack:
        current = stack.pop()
        if current == end:
            return True
        if road[current]:
            for node in road[current]:
                visited[node] = True
                stack.append(node)
    return False


for _ in range(T):
    testcase, road_cnt = map(int, input().split())

    road = [[] for _ in range(road_size)]
    road_list = list(map(int, input().split()))
    visited = [False for _ in range(road_size)]

    # [(start, end), (start, end) ...] 순서쌍이므로
    for idx in range(0, len(road_list), 2):
        road[road_list[idx]].append(road_list[idx+1])

    isArrived = dfs(start_city, end_city)

    print(f'#{testcase}', end=' ')
    if isArrived:
        print(1)
    else:
        print(0)
