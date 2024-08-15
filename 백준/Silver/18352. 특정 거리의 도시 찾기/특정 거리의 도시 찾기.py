from collections import deque
# N : 도시의 개수
# M : 도로의 개수
# K : 거리 정보
# X : 출발 도시 번호
N, M, K, X = map(int, input().split())

roads = [[] for _ in range(N+1)]
distance = [-1] * (N+1)
distance[X] = 0

def bfs(start):
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for road in roads[current]:
            if distance[road] == -1:
                distance[road] = distance[current] + 1
                queue.append(road)

for _ in range(M):
    st, ed = map(int, input().split())
    roads[st].append(ed)

bfs(X)
result = []

for idx in range(N+1):
    if distance[idx] == K:
        result.append(idx)

if result:
    print(*result, sep='\n')
else:
    print(-1)