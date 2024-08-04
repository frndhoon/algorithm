T = int(input())

def get_cnt(x, y):

    cnt = 0
    for nx in range(0, n):
        cnt += matrix[nx][y]
    for ny in range(0, n):
        cnt += matrix[x][ny]
    
    # 중앙 값 중복 제거
    return cnt - matrix[x][y]


for testcase in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    # 초기값 설정
    min_cnt = max_cnt = get_cnt(0, 0)

    for x in range(n):
        for y in range(n):
            cnt = get_cnt(x, y)
            if cnt > max_cnt:
                max_cnt = cnt
            if cnt < min_cnt:
                min_cnt = cnt

    print(f'#{testcase} {max_cnt - min_cnt}')
