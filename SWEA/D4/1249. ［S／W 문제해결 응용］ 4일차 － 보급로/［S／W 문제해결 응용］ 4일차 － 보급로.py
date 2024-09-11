# 다익스트라
import heapq
INF = int(1e8)


def dijkstra(start_y=0, start_x=0):
    """
    다익스트라
    :param start_y: 시작 y좌표
    :param start_x: 시작 x좌표
    :return:
    """
    min_heap = []
    heapq.heappush(min_heap, (0, start_y, start_x))
    distances[start_y][start_x] = 0

    while min_heap:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, current_y, current_x = heapq.heappop(min_heap)

        # 현재 노드가 이미 처리된 적이 있다면 무시
        if distances[current_y][current_x] < dist:
            continue

        for dir_y, dir_x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current_y + dir_y, current_x + dir_x

            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N: continue

            # 현재 지점에서 다음 지점의 거리 확인
            next_dist = distances[current_y][current_x] + matrix[next_y][next_x]

            # 다음 지점에 저장된 거리가 더 멀 때만 갱신
            if distances[next_y][next_x] > next_dist:
                distances[next_y][next_x] = next_dist
                heapq.heappush(min_heap, (next_dist, next_y, next_x))


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    distances = [[INF] * N for _ in range(N)]

    dijkstra()

    print(f'#{testcase} {distances[N-1][N-1]}')
