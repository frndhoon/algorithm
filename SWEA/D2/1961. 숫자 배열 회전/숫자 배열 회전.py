T = int(input())

for testcase in range(1, T+1):
    size = int(input())

    matrix = [list(map(int, input().split())) for _ in range(size)]

    matrix_90 = list(zip(*matrix[::-1]))
    matrix_180 = list(zip(*matrix_90[::-1]))
    matrix_270 = list(zip(*matrix_180[::-1]))

    print(f'#{testcase}')
    for rotate_90, rotate_180, rotate_270 in zip(matrix_90, matrix_180, matrix_270):
        print(*rotate_90, end=' ', sep='')
        print(*rotate_180, end=' ', sep='')
        print(*rotate_270, sep='')
