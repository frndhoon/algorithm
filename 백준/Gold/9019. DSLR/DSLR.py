from collections import deque

testcase = int(input())


def bfs(init_num, final_num):

    queue = deque([(init_num, '')])
    # 숫자 방문 여부
    visited = [False] * 10001

    while queue:
        num, cmd = queue.popleft()
        
        if num == final_num:
            return cmd
        
        D_result = (num * 2) % 10000
        S_result = (num - 1) % 10000
        L_result = (num % 1000) * 10 + (num // 1000)
        R_result = (num % 10) * 1000 + (num // 10)
        
        # 숫자 중복 방문하지 않았다면, queue에 추가
        if not visited[D_result]:
            queue.append((D_result, cmd + 'D'))
            visited[D_result] = True

        if not visited[S_result]:
            queue.append((S_result, cmd + 'S'))
            visited[S_result] = True

        if not visited[L_result]:
            queue.append((L_result, cmd + 'L'))
            visited[L_result] = True

        if not visited[R_result]:
            queue.append((R_result, cmd + 'R'))
            visited[R_result] = True


for _ in range(testcase):
    init_num, final_num = map(int, input().split())
    result = bfs(init_num, final_num)

    print(result)
