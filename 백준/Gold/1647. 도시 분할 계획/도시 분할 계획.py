def find(x):
    """
    특정 원소가 속한 집합 찾기
    :param x: 특정 원소
    :return:
    """
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    """
    두 원소가 속한 집합 찾아서 합치기
    :param a: 원소1
    :param b: 원소2
    :return:
    """
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        if rootA < rootB:
            parents[rootB] = rootA
        elif rootA > rootB:
            parents[rootA] = rootB


house_cnt, road_cnt = map(int, input().split())

parents = [i for i in range(house_cnt+1)]

edges = []
for _ in range(road_cnt):
    start_house, end_house, cost = map(int, input().split())
    edges.append((cost, start_house, end_house))


edges.sort()
used_edges = []

min_cost_by_merged_house = 0

for cost, start, end in edges:
    if find(start) != find(end):
        union(start, end)
        min_cost_by_merged_house += cost
        used_edges.append(cost)

        if len(used_edges) == house_cnt - 1:
            break

# 가장 비용이 큰 간선을 제거하면 두 개의 분리된 집이 됨
min_cost_by_two_separated_house = min_cost_by_merged_house - max(used_edges)

print(min_cost_by_two_separated_house)
