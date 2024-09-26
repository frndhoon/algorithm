from collections import deque

def bfs(start, end):
    queue = deque([(start, 0)])
    visited = [[-1, 0] for _ in range(200001)]  # [최소 시간, 방법의 수]
    visited[start] = [0, 1]

    while queue:
        current, time = queue.popleft()

        for next in (current-1, current+1, current*2):
            if 0 <= next <= 200000:
                if visited[next][0] == -1:  # 첫 방문
                    visited[next] = [time + 1, visited[current][1]]
                    queue.append((next, time + 1))
                elif visited[next][0] == time + 1:  # 같은 시간에 다시 방문
                    visited[next][1] += visited[current][1]

    return visited[end]

subin_location, child_location = map(int, input().split())
min_time, count = bfs(subin_location, child_location)
print(min_time)
print(count)