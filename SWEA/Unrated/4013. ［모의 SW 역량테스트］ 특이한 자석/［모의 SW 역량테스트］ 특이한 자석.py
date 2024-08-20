from collections import deque
T = int(input())
DIRS = [-1, 1]
cnt = 4

for testcase in range(1, T+1):
    # 자석 회전 횟수
    K = int(input())
    # 자석 정보
    matrix = [deque(list(map(int, input().split()))) for _ in range(cnt)]
    answer = 0

    for _ in range(K):
        temp = matrix[:]
        # [1] 회전 방향 저장, (1: 시계, -1: 반시계, 0: 회전X)
        is_rotate = [0] * cnt

        num, rotate = map(int, input().split())
        num -= 1  # index 0부터 시작함
        is_rotate[num] = rotate

        queue = deque([(num, rotate)])
        visited = set()
        visited.add(num)

        while queue:
            c, r = queue.popleft()
            # 양 옆 탐색
            for dx in DIRS:
                nx = dx + c

                if 0 <= nx < cnt and nx not in visited:
                    # 자석의 맞닿은 부분의 극이 다르면
                    if (dx == 1 and temp[c][2] != temp[nx][-2]) or (dx == -1 and temp[c][-2] != temp[nx][2]):
                        is_rotate[nx] = -r  # 자석이 반대 방향으로 회전
                        visited.add(nx)
                        queue.append((nx, -r)) # 회전 방향 반대로 해서 저장

        # [2] 회전 유무로 시계방향(1), 반시계방향(-1)으로 회전시키기
        for i in range(cnt):
            if is_rotate[i] == 1:
                temp[i].appendleft(temp[i].pop())
            elif is_rotate[i] == -1:
                temp[i].append(temp[i].popleft())

        matrix = temp[:]

    # [3] 각 자석의 0번째가 S면, 1 2 4 8 순으로 획득
    for i in range(cnt):
        if matrix[i][0] == 1:
            answer += 2 ** i

    print(f'#{testcase} {answer}')
