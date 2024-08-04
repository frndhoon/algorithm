T = int(input())

def get_fly(matrix, x, y, size):
    fly = 0
    # 사각형 범위의 넓이이므로 그만큼 탐색
    for i in range(x, x+size):
        for j in range(y, y+size):
            fly += matrix[i][j]
    return fly

for testcase in range(1, T+1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    max_fly = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            fly = get_fly(matrix, i, j, m)
            if fly > max_fly:
                max_fly = fly

    print(f'#{testcase} {max_fly}')
