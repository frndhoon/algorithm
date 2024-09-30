import heapq

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    # 양방향 저장
    graph[start].append((end, cost))
    graph[end].append((start, cost))

target_point1, target_point2 = map(int, input().split())


def dijkstra(start):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    pq = [(distances[start], start)] # 1번 정점부터 시작

    while pq:
        dist, current = heapq.heappop(pq)

        if distances[current] < dist: continue

        for next, next_dist in graph[current]:
            total_dist = distances[current] + next_dist
            if distances[next] > total_dist:
                distances[next] = total_dist
                heapq.heappush(pq, (total_dist, next))

    return distances


start_distances = dijkstra(1)
target1_distances = dijkstra(target_point1)
target2_distances = dijkstra(target_point2)

# 두 개의 정점을 지나는 최단 경로의 길이 출력
min_distance = float('inf')
min_distance = min(start_distances[target_point1] + target1_distances[target_point2] + target2_distances[N],
                   start_distances[target_point2] + target2_distances[target_point1] + target1_distances[N])


print(min_distance if min_distance != float('inf') else -1)
