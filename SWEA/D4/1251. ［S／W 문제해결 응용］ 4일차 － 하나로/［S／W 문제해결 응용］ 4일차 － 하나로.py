import heapq
T = int(input())


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        if rootA < rootB:
            parents[rootB] = rootA
        else:
            parents[rootA] = rootB


for testcase in range(1, T+1):
    island_cnt = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    pq = []

    for i in range(island_cnt-1):
        for j in range(i+1, island_cnt):
            distance = abs(x_list[i] - x_list[j]) ** 2 + abs(y_list[i] - y_list[j]) ** 2
            heapq.heappush(pq, (distance, i, j))

    parents = [i for i in range(island_cnt)]

    # 환경 부담 세율
    E = float(input())
    min_dist = 0

    while pq:
        dist, start, end = heapq.heappop(pq)

        
        if parents.count(0) == island_cnt:
            break

        if find(start) != find(end):
            min_dist += dist
            union(start, end)

    print(f'#{testcase} {round(min_dist*E)}')