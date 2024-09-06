from collections import deque

def bfs(group):  # 이어진지 체크
    queue = deque([group[0]])
    visited = {group[0]}

    while queue:
        current_row, current_col = queue.popleft()
        for dir_row, dir_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = current_row + dir_row, current_col + dir_col
            if (next_row, next_col) in group and (next_row, next_col) not in visited:  # 연결됐는지 확인
                queue.append((next_row, next_col))
                visited.add((next_row, next_col))

    return len(visited) == len(group)  # 방문한 것과 원래 그룹이 같다면 True

N = 5
matrix = [list(input()) for _ in range(N)]
case_cnt = 0


def combination(idx=0, lst=[], som_cnt=0):
    global case_cnt

    if len(lst) == 7:  # 7공주가 모였고,
        if som_cnt >= 4 and bfs(lst):  # 이다솜파가 4명 이상이고 이어져 있을 때
            case_cnt += 1
        return

    if idx == N*N:
        return

    row, col = idx // N, idx % N

    # 현재 학생을 선택하는 경우
    lst.append((row, col))
    combination(idx+1, lst, som_cnt + (1 if matrix[row][col] == 'S' else 0))
    lst.pop()

    # 현재 학생을 선택하지 않는 경우
    combination(idx+1, lst, som_cnt)


combination()

print(case_cnt)
