def find(x):
    """
    특정 원소가 속한 집합 찾기
    :param x: 특정 원소
    :return:
    """
    if parent[x] != x:  # 자기 자신이 부모가 아니라면
        parent[x] = find(parent[x])  # 거슬러 올라가면서 부모 값 갱신
    return parent[x]

def union(a, b):
    """
    두 원소가 속한 집합 찾기
    :param a: 원소1
    :param b: 원소2
    :return:
    """
    rootA = find(a)  # 원소1의 부모 찾기
    rootB = find(b)  # 원소2의 부모 찾기

    if rootA == rootB:
        return

    if rootA != rootB:
        # rank를 비교하여 더 작은 트리를 큰 트리 밑에 병합
        if rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        elif rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            # rank가 같으면 한쪽을 다른 쪽 아래로 병합하고 rank를 증가시킴
            parent[rootB] = rootA
            rank[rootA] += 1


edges = []

V, E = map(int, input().split())
parent = [0] * (V+1)
rank = [0] * (V+1)

for i in range(1, V+1):
    parent[i] = i

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, b, a))  # 가중치 오름차순 정렬

edges.sort()

result = 0  # 최소 가중치를 넣을 변수
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)