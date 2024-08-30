# dfs
# [1] dfs 탐색
def dfs(start):
    stack = [start]
    known[start] = True

    while stack:
        current = stack.pop()
        for man in graph[current]:
            if not known[man]:
                known[man] = True
                stack.append(man)


T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())  # N : 사람 명수, M : 관계 수

    graph = [[] for _ in range(N+1)]
    known = [False] * (N + 1)

    for _ in range(M):
        st, ed = map(int, input().split())
        graph[st].append(ed)
        graph[ed].append(st)

    cnt = 0

    # [2] 모르는 관계일 때만 탐색 시작
    for man in range(1, N+1):
        if not known[man]:
            dfs(man)
            cnt += 1

    print(f'#{testcase} {cnt}')