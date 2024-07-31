T = int(input())


for testcase in range(1, T+1):
    # 빨강, 파랑 칠할 list 저장
    grid = [[[0, 0] for _ in range(10)] for _ in range(10)]
    n = int(input())
    purple = 0

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                grid[x][y][color - 1] += 1

    for x in range(10):
        for y in range(10):
            # 둘 다 칠해져있으면
            if grid[x][y] == [1, 1]:
                purple += 1

    print(f'#{testcase} {purple}')
