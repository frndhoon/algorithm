# bfs
ROW, COL = 12, 6
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우


# [1] 같은 색 뿌요 4개 이상 모였는지 체크
def check_puyo(r, c, current_color):
    visited = [[False] * COL for _ in range(ROW)]
    puyo_cnt = 1
    stack = [(r, c)]
    bang_list = [(r, c)]
    visited[r][c] = True

    while stack:
        cr, cc = stack.pop()
        for dr, dc in DIRECTIONS:
            nr, nc = dr + cr, dc + cc
            if 0 <= nr < ROW and 0 <= nc < COL and not visited[nr][nc] and matrix[nr][nc] == current_color:
                visited[nr][nc] = True
                stack.append((nr, nc))
                bang_list.append((nr, nc))
                puyo_cnt += 1

    if puyo_cnt >= 4:  # 뿌요가 4 이상이여야 터짐
        return bang_list
    return []

# [2] 터뜨리기
def bang(bang_list):
    for bang_r, bang_c in bang_list:
        matrix[bang_r][bang_c] = '.'


# [3] 밑으로 내리기
def push_down():
    for c in range(COL):
        temp = []
        for r in range(ROW - 1, -1, -1):
            if matrix[r][c] != '.':
                temp.append(matrix[r][c])

        for r in range(ROW - 1, -1, -1):
            if temp:
                matrix[r][c] = temp.pop(0)
            else:
                matrix[r][c] = '.'


matrix = [list(input()) for _ in range(ROW)]
chain_cnt = 0

# 메인 로직
while True:
    exploded = False
    for r in range(ROW):
        for c in range(COL):
            if matrix[r][c] != '.':  # 뿌요라면, bang_list 받기
                bang_list = check_puyo(r, c, matrix[r][c])
                if bang_list:  # bang_list가 있다면, 터뜨리기
                    bang(bang_list)
                    exploded = True
    if exploded: # 폭발됐다면, 
        chain_cnt += 1  # 연쇄 폭발 += 1
        push_down()
    else:
        break

# [result] 연쇄가 몇 번 되는지 출력, 하나도 터지지 않는다면 0을 출력
print(chain_cnt)