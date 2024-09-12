import heapq
INF = int(1e9)

def dijkstra(start):
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if distances[current_node] < current_dist: continue

        for next_node, next_dist in graph[current_node]:
            dist = current_dist + next_dist
            if distances[next_node] > dist:
                distances[next_node] = dist
                heapq.heappush(pq, (dist, next_node))


N = int(input())  # 도시의 개수 (정점)
M = int(input())  # 버스의 개수 (간선)

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, dist = map(int, input().split())
    graph[s].append((e, dist))

start, end = map(int, input().split())  # 출발 도시에서 도착 도시까지 가는 데 드는 최소 비용

distances = [INF] * (N+1)

dijkstra(start)

print(distances[end])

