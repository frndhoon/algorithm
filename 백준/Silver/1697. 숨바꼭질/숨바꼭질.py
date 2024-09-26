from collections import deque
subin_location, child_location = map(int, input().split())


def bfs():
    queue = deque([(subin_location, 0)])
    visited = {subin_location}

    while queue:
        current, time = queue.popleft()

        if current == child_location:
            return time

        for next in (current-1, current+1, current*2):
            if next < 0 or next > 100000: continue
            if next in visited: continue

            visited.add(next)
            queue.append((next, time+1))


answer = bfs()
print(answer)