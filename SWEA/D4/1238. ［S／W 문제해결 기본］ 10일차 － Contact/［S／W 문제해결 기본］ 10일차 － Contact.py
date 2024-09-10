import heapq
from collections import deque, defaultdict


def bfs(start):
    """
    bfs
    :param start: 시작 지점
    :return: 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람
    """
    queue = deque([(start, 0)])
    max_heap = [(-0, -start)]  # 횟수, 시작지점 (최대 힙) => 번호가 가장 큰 사람을 구해야함
    visited = set([start])

    while queue:
        current_man, cnt = queue.popleft()

        for next_man in contacts[current_man]:
            if next_man in visited: continue

            visited.add(next_man)
            queue.append((next_man, cnt + 1))
            heapq.heappush(max_heap, (-(cnt + 1), -next_man))

    return -heapq.heappop(max_heap)[1]


T = 10
for testcase in range(1, T + 1):
    data_len, start_point = map(int, input().split())
    contact_data = list(map(int, input().split()))
    contacts = defaultdict(list)

    for i in range(0, data_len, 2):
        start, end = contact_data[i], contact_data[i + 1]
        contacts[start].append(end)

    result = bfs(start_point)

    # [result] 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람
    print(f'#{testcase} {result}')
