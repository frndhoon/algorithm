import heapq
INF = float('inf')

def dijkstra(start):
    """
    다익스트라
    :param start: 시작 지점
    :return : 최소 시간들(list)
    """

    distances = [INF] * (student_cnt+1)
    distances[start] = 0
    pq = [(distances[start], start)]

    while pq:
        dist, current = heapq.heappop(pq)

        if distances[current] < dist: continue

        for next, next_dist in graph[current]:
            dist_sum = distances[current] + next_dist

            if distances[next] > dist_sum:
                distances[next] = dist_sum
                heapq.heappush(pq, (dist_sum, next))

    return distances


student_cnt, road_cnt, target_house = map(int, input().split())

graph = [[] for _ in range(student_cnt+1)]
for _ in range(road_cnt):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

max_time = 0
min_distances_by_target_house = dijkstra(target_house)
for i in range(1, student_cnt+1):
    if i == target_house:  # 목표 마을은 건너뛰기
        continue
    min_distances = dijkstra(i)
    # 목표 마을로 갔다가 다시 자기 집으로 가는 것 가장 오래 걸리 학생의 소요시간
    max_time = max(max_time, min_distances_by_target_house[i] + min_distances[target_house])

print(max_time)
