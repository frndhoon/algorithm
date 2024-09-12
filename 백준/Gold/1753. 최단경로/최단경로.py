import heapq

def dijkstra(start=1):
    distances[start] = 0
    pq = [(distances[start], start)]

    while pq:
        cost, node = heapq.heappop(pq)
        if distances[node] < cost: continue

        for next_node, next_cost in graph[node]:
            total_cost = cost + next_cost
            if distances[next_node] > total_cost:
                distances[next_node] = total_cost
                heapq.heappush(pq, (total_cost, next_node))


V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = int(1e6)
distances = [INF] * (V+1)

dijkstra(K)
for dist in distances[1:]:
    print(dist if dist != INF else 'INF')