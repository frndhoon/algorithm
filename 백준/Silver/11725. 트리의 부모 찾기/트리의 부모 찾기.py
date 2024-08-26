N = int(input())

lst = [[] for _ in range(N+1)]
parent = [0] * (N+1)  # 부모 노드 저장

for _ in range(N-1):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

def dfs(start=1):
    stack = [start]
    while stack:
        current = stack.pop()
        for i in lst[current]:
            if parent[i] == 0:
                parent[i] = current
                stack.append(i)

dfs()
print('\n'.join(map(str, parent[2:])))