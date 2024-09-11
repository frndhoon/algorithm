import heapq
INF = int(1e6)


def dijkstra(start=0):

    distances[start] = 0
    pq = [(distances[start], start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for node, dist in edges[current_node]:
            next_dist = distances[current_node] + dist

            if distances[node] > next_dist:
                distances[node] = next_dist
                heapq.heappush(pq, (distances[node], node))


T = int(input())
for testcase in range(1, T+1):
    N, E = map(int, input().split())
    edges = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        edges[s].append((e, w))

    distances = [INF] * (N + 1)

    dijkstra()
    
    # 끝 지점의 갱신된 최단 거리
    result = distances[-1]
    print(f'#{testcase} {result}')