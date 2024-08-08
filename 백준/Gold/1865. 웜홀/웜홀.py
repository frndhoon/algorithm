T = int(input())
INF = int(1e9)


def bf():
    # 어느 점을 기준으로 해도 상관없음
    dist[1] = 0

    # 지점의 개수만큼 반복
    for i in range(point_cnt):
        # 매번 모든 도로를 탐색
        for start, end, cost in road:
            # 현재 도로를 거쳐 다른 지점으로 이동하는 거리가 더 짧은 경우 갱신
            if dist[end] > dist[start] + cost:
                dist[end] = dist[start] + cost
                # 지점을 다 돌았는데도 값이 갱신된다면, 음수 순환이 존재한다는 뜻 (시간이 단축된다는 뜻)
                if i == point_cnt - 1:
                    return True
    return False


for _ in range(T):
    point_cnt, road_cnt, wormhole_cnt = map(int, input().split())
    road = []
    # 최단 거리 테이블 무한으로 초기화
    dist = [INF] * (point_cnt + 1)

    for _ in range(road_cnt):
        connect_start, connect_end, cost = map(int, input().split())
        road.append((connect_start, connect_end, cost))
        road.append((connect_end, connect_start, cost))

    # 웜홀은 시간이 단축됨
    for _ in range(wormhole_cnt):
        start, end, minus_cost = map(int, input().split())
        road.append((start, end, -minus_cost))

    is_time_decrease = bf()

    if is_time_decrease:
        print('YES')
    else:
        print('NO')
