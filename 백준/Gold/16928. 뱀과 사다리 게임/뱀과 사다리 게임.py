from collections import defaultdict, deque

ladder_cnt, snake_cnt = map(int, input().split())

ladders = defaultdict(list)
snakes = defaultdict(list)

for _ in range(ladder_cnt):
    st, ed = map(int, input().split())
    ladders[st] = ed

for _ in range(snake_cnt):
    st, ed = map(int, input().split())
    snakes[st] = ed


def bfs(start=1, cnt=0):
    """
    bfs 탐색
    :param start: 시작 좌표
    :param cnt: 주사위 횟수
    :return:
    """

    queue = deque([(start, cnt)])
    visited = {start}

    while queue:
        current, current_cnt = queue.popleft()
        if current == 100:
            return current_cnt

        for i in range(1, 7):
            next = current + i

            if next > 100: continue
            
            if next in ladders:  # 사다리가 있으면 타기
                next = ladders[next]
            if next in snakes:  # 뱀이 있다면 뱀 타기
                next = snakes[next]

            if next in visited: continue

            visited.add(next)
            queue.append((next, current_cnt + 1))


answer = bfs()
print(answer)
