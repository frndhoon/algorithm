import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def dijkstra(start):
    distances[start] = 0
    pq = [(distances[start], start)]

    while pq:
        cost, node = heapq.heappop(pq)

        if distances[node] < cost: continue

        for next_node, next_cost in graph[node]:
            total_cost = cost + next_cost
            if total_cost < distances[next_node]:
                distances[next_node] = total_cost
                prev_node[next_node] = node  # 거리가 갱신될 경우 가까운 노드 저장
                heapq.heappush(pq, (total_cost, next_node))


INF = int(1e8)


city_cnt = int(input())  # 정점의 개수
bus_cnt = int(input())  # 간선의 개수

graph = defaultdict(list)

for _ in range(bus_cnt):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))

distances = [INF] * (city_cnt + 1)
prev_node = [0] * (city_cnt + 1)

start_city, end_city = map(int, input().split())

dijkstra(start_city)

path = [end_city]
now = end_city
while now != start_city:  # 처음 도시에 갈 때까지 경로 저장
    now = prev_node[now]
    path.append(now)

path.reverse()

print(distances[end_city])
print(len(path))
print(*path)