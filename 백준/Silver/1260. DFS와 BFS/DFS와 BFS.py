from collections import deque
N, M, V = map(int, input().split())

tbl = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    tbl[s].append(e)
    tbl[e].append(s)

for t in tbl:
    t.sort()


def dfs(start):
    visited = set()
    stk = [start]

    while stk:
        v = stk.pop()
        if v not in visited:
            visited.add(v)
            print(v, end=' ')
            for neighbor in reversed(tbl[v]):
                if neighbor not in visited:
                    stk.append(neighbor)
    print()


def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in tbl[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()


dfs(V)
bfs(V)