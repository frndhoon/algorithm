T = int(input())


def get_cnt(matrix, digit):
    length = len(matrix)
    # 현재 matrix에서 찾을 수 있는 자리의 수
    result = 0

    for x in range(length):
        # 자리수 카운팅
        cnt = 0
        for y in range(length):
            if matrix[x][y] == 0:
                # 자리수가 목표와 같다면, +1
                if cnt == digit:
                    result += 1
                cnt = 0
            else:
                cnt += 1

        # 마지막 자리수 1일 때 한번 더 판단
        if cnt == digit:
            result += 1

    return result


for testcase in range(1, T+1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # 90도 돌려서 찾기
    matrix_90 = list(zip(*matrix[::-1]))

    result = get_cnt(matrix, k) + get_cnt(matrix_90, k)

    print(f'#{testcase} {result}')

