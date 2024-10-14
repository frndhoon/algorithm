import heapq

MIN_POINT = 0
MAX_POINT = 100000

subin_location, brother_location = map(int, input().split())


def dijkstra(start: int, end: int) -> int:
    """
    다익스트라 알고리즘
    :param start: 시작 지점(수빈)
    :param end: 도착 지점(동생)
    :return: 수빈이가 동생을 찾는 가장 빠른 시간
    """
    distances = [float('inf')] * (MAX_POINT + 1)
    distances[start] = 0

    pq = [(distances[start], start)]

    while pq:
        current_dist, current_point = heapq.heappop(pq)

        if distances[current_point] < current_dist: continue # 갱신될 필요 없는 경우 패스

        # 이동 가능한 경우
        for next_point in (current_point - 1, current_point + 1, current_point * 2):
            if next_point < MIN_POINT or next_point > MAX_POINT:
                continue

            # 이동 거리 계산
            if next_point == current_point * 2:
                next_dist = current_dist  # 순간이동
            else:
                next_dist = current_dist + 1  # 걷기

            if distances[next_point] > next_dist:
                distances[next_point] = next_dist
                heapq.heappush(pq, (next_dist, next_point))

    return distances[end]

print(dijkstra(subin_location, brother_location))