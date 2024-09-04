# [1] 공격받을 수 있는 지 판단
def can_attacked(row):
    for r in range(row):
        # 같은 행이거나 대각선에 위치해있을 때, 공격받음
        if column[row] == column[r] or row - r == abs(column[row] - column[r]):
            return True
    return False


# [2] 퀸 놓기
def n_queen(row=0):
    global not_attacked_each_queen_cnt
    if row == N:  # 행 끝까지 퀸이 놓아졌다면,
        not_attacked_each_queen_cnt += 1
        return

    for col in range(N):  # 열 탐색
        column[row] = col  # 행의 열에 퀸 놓기
        if not can_attacked(row):  # 가지치기
            n_queen(row+1)


T = int(input())

for testcase in range(1, T+1):
    not_attacked_each_queen_cnt = 0

    N = int(input())

    column = [-1] * N  # 열 체크
    
    n_queen()
    
    # N x N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는?
    print(f'#{testcase} {not_attacked_each_queen_cnt}')
