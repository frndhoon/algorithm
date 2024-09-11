import heapq
INF = int(1e6)
# 다익스트라

def dijkstra(start):
    distances = [INF] * (V + 1)
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

    return distances


T = int(input())
for testcase in range(1, T+1):

    V, E, target_house = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        st, ed, d = map(int, input().split())
        edges[st].append((ed, d))

    max_dist = 0

    target_dist = dijkstra(target_house)
    
    for i in range(1, V+1):
        current_dist = dijkstra(i)
        if current_dist[target_house] + target_dist[i] < INF:
            max_dist = max(max_dist, current_dist[target_house] + target_dist[i])

    # [result] 오고 가는데 걸리는 시간이 가장 긴 거리 출력력
    print(f'#{testcase} {max_dist}')
