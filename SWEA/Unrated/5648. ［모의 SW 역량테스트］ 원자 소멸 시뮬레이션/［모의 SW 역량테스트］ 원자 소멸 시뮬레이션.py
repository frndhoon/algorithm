T = int(input())
 
for testcase in range(1, T+1):
    N = int(input())
    score = 0
 
    # x, y, 방향, 에너지
    atom = [list(map(int, input().split())) for _ in range(N)]
 
    # [1] 좌표 두 배, 기존 원소 저장
    for i in range(N):
        atom[i][0] *= 2
        atom[i][1] *= 2
 
    for _ in range(4001):  # 원소 -2000에서 2001까지 가는 최대 거리
        # [2] 원소 이동(동시에)
        for i in range(len(atom)):
            dir = atom[i][2]
            if dir == 0:
                atom[i][1] += 1
            elif dir == 1:
                atom[i][1] -= 1
            elif dir == 2:
                atom[i][0] -= 1
            elif dir == 3:
                atom[i][0] += 1
 
        # [3] 같은 위치 원소
        visited = set()
        crashed = set()
        for i in range(len(atom)):
            if (atom[i][0], atom[i][1]) in visited:
                crashed.add((atom[i][0], atom[i][1]))
            else:
                visited.add((atom[i][0], atom[i][1]))
 
        # [4] 점수 계산
        for i in range(len(atom)-1, -1, -1):
            if (atom[i][0], atom[i][1]) in crashed: # 충돌됐으면
                score += atom[i][3]
                atom.pop(i)
            elif abs(atom[i][0]) > 2000 and abs(atom[i][1]) > 2000:  # 범위 밖이면
                atom.pop(i)
 
    print(f'#{testcase} {score}')