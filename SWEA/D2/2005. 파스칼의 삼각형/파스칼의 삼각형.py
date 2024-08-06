T = int(input())


def memorize(n):
    if len(memo) >= n:
        return memo[:n]

    for i in range(len(memo)-1, n):
        new_arr = [1]
        for j in range(1, len(memo[i])):
            new_arr.append(memo[i][j-1] + memo[i][j])
        new_arr.append(1)
        memo.append(new_arr)

    return memo[:n]


memo = [[1], [1, 1]]

for testcase in range(1, T + 1):
    n = int(input())
    print(f'#{testcase}')

    result = memorize(n)
    for row in result:
        print(' '.join(map(str, row)))
