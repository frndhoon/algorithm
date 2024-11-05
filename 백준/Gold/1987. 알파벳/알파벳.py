def dfs(r, c, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            # ord(알파벳) - ord('A')를 인덱스로 사용
            alphabet_idx = ord(board[nr][nc]) - ord('A')
            if not visited[alphabet_idx]:  # 알파벳이 아직 사용되지 않았다면
                visited[alphabet_idx] = True
                dfs(nr, nc, cnt + 1)
                visited[alphabet_idx] = False

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
max_cnt = 1
# 알파벳 개수(26)만큼의 방문 체크 배열
visited = [False] * 26
# 시작 위치 방문 체크
visited[ord(board[0][0]) - ord('A')] = True
dfs(0, 0, 1)
print(max_cnt)