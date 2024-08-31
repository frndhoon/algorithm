# [1] 트리 탐색
def dfs(start):
    is_cycle = False
    stack = [start]

    while stack:
        current = stack.pop()
        if visited[current]:  # 이미 방문한 정점이면 사이클 체크 (트리 안됨)
            is_cycle = True
        visited[current] = True
        for v in trees[current]:
            if not visited[v]:
                stack.append(v)

    return is_cycle


testcase = 0
while True:
    testcase += 1
    # 테스트 케이스별 정점 개, 간선 개수
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    trees = [[] for _ in range(n+1)]
    for _ in range(m):
        st, ed = map(int, input().split())
        trees[st].append(ed)
        trees[ed].append(st)

    visited = [False] * (n+1)

    tree_cnt = 0
    for v in range(1, n + 1):
        if visited[v]:
            continue
        if not dfs(v):
            tree_cnt += 1

    print(f'Case {testcase}:', end=' ')
    if tree_cnt == 0:
        print('No trees.')
    elif tree_cnt == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {tree_cnt} trees.')