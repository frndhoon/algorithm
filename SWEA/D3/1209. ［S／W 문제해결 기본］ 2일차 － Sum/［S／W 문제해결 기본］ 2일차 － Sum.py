T = 10
arr_len = 100


# 대각선 합
def get_diagonal_sum(arr):
    n = arr_len

    left_diagonal_sum = 0
    right_diagonal_sum = 0

    for i in range(n):
        left_diagonal_sum += arr[i][i]
        right_diagonal_sum += arr[i][n - 1 - i]

    if left_diagonal_sum > right_diagonal_sum:
        return left_diagonal_sum
    else:
        return right_diagonal_sum


# 행, 열 합
def get_row_col_sum(arr):
    n = arr_len

    max_sum = 0

    for i in range(n):
        row_sum = 0
        col_sum = 0

        for j in range(n):
            row_sum += arr[i][j]
            col_sum += arr[j][i]

        if row_sum > max_sum:
            max_sum = row_sum
        if col_sum > max_sum:
            max_sum = col_sum

    return max_sum


for _ in range(T):
    testcase = input()
    arr = [list(map(int, input().split())) for _ in range(arr_len)]

    max_sum = 0

    max_row_col_sum = get_row_col_sum(arr)
    diagonal_sum = get_diagonal_sum(arr)

    if max_row_col_sum > diagonal_sum:
        max_sum = max_row_col_sum
    else:
        max_sum = diagonal_sum

    print(f'#{testcase} {max_sum}')

