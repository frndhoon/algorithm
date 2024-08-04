T = int(input())
max_bus_stop = 5001

for testcase in range(1, T+1):
    n = int(input())
    bus_stop = [0] * max_bus_stop

    for _ in range(n):
        # 시작점부터 끝점까지 버스 정류장 노선을 다니는 버스 개수 체크
        start, end = map(int, input().split())
        for idx in range(start, end + 1):
            bus_stop[idx] += 1

    bus_stop_num = int(input())

    # 출력할 특정 버스 정류장 노선
    bus_stop_list = []
    for _ in range(bus_stop_num):
        bus_stop_list.append(int(input()))

    print(f'#{testcase}', end=' ')
    for idx in bus_stop_list:
        print(f'{bus_stop[idx]}', end=' ')
    print()