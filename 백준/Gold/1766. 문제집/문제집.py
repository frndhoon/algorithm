import heapq
N, M = map(int, input().split())
indegrees = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    front, back = map(int, input().split())
    graph[front].append(back)
    indegrees[back] += 1

def topo_sort():
    pq = []
    result = []
    for i in range(1, N+1):
        if indegrees[i] == 0:
            # 가능하면 쉬운 문제부터 풀기
            heapq.heappush(pq, i)

    while pq:
        #
        current = heapq.heappop(pq)
        result.append(current)

        for i in graph[current]:
            indegrees[i] -= 1
            if indegrees[i] == 0:
                heapq.heappush(pq, i)
        # 항상 문제를 풀 수 있는 경우만 존재

    return result

result = topo_sort()
print(*result, sep=' ')