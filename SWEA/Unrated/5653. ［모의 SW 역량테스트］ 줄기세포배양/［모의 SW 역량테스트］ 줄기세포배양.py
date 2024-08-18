import heapq

T = int(input())
DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for testcase in range(1, T+1):
    # N x M (최대 50 x 50)
    # K시간 만큼 배양
    N, M, K = map(int, input().split())
    badge = [list(map(int, input().split())) for _ in range(N)]
    activate = []  # 살아 있는 줄기 세포
    temp = []  # cycle 간 임시 저장해줄 list
    cell_grid = set()  # 줄기 세포가 존재하는 그리드 저장

    for i in range(N):
        for j in range(M):
            if badge[i][j] != 0:
                # 파이썬은 기본 최소 힙이므로 내림차순 시 -로 저장
                heapq.heappush(activate, (-badge[i][j], i, j, 0))  # 생명력, 좌표, 활성화시간
                cell_grid.add((i, j))

    # K시간 만큼 반복
    for _ in range(K):
        while activate:
            life, x, y, activate_time = heapq.heappop(activate)
            life = -life  # -로 저장했으니 원래대로 원상복귀

            if life > activate_time:  # 비활성화 시 활성화 시간 +1
                heapq.heappush(temp, (-life, x, y, activate_time + 1))

            elif life * 2 > activate_time + 1:  # 2 * 목숨 시간 까지 살아 남음
                heapq.heappush(temp, (-life, x, y, activate_time + 1))

            if life == activate_time: # 활성화 시, 탐색
                for dx, dy in DELTAS:
                    nx, ny = dx + x, dy + y
                    if (nx, ny) not in cell_grid:
                        cell_grid.add((nx, ny))
                        heapq.heappush(temp, (-life, nx, ny, 0))  # 우선 순위가 높은(생명력 수치가 높은) 줄기 세포가 먼저 탐색됨

        activate = temp[:]  # 한 사이클 돌면, 활성화 세포로 할당
        temp = []

    print(f'#{testcase} {len(activate)}')  # K시간 후 살아 있는 줄기 세포(비활성+활성 상태) 개수
