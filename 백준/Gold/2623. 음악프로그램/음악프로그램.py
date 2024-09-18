from collections import deque
N, M = map(int, input().split())
indegrees = [0] * (N + 1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    singer_list = list(map(int, input().split()))
    for i in range(1, len(singer_list)-1):
        graph[singer_list[i]].append(singer_list[i+1])
        indegrees[singer_list[i + 1]] += 1

# 위상 정렬
def topo_sort():
    queue = deque()
    result = []
    for idx in range(1, N+1):
        if indegrees[idx] == 0:
            queue.append(idx)

    while queue:
        current = queue.popleft()
        result.append(current)

        for idx in graph[current]:
            indegrees[idx] -= 1
            if indegrees[idx] == 0:
                queue.append(idx)

    if len(result) != N:  # 사이클 존재하는 지 판단
        return [0]

    return result


answer = topo_sort()

print(*answer, sep='\n')
