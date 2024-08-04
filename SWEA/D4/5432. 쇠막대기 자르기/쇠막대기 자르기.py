T = int(input())

for testcase in range(1, T+1):
    sliver_rod = list(input())
    rod = 0
    cnt = 0

    for idx in range(len(sliver_rod)):
        # 열렸으면 막대 만들기
        if sliver_rod[idx] == '(':
            rod += 1
        
        # 닫혔으면 레이저 or 막대 끝
        elif sliver_rod[idx] == ')':
            # 연속됐으면 레이저로 열린 막대 수만큼 자르기
            if sliver_rod[idx - 1] == '(':
                rod -= 1
                cnt += rod
            # 아니라면 막대 마지막 조각 카운트
            else:
                rod -= 1
                cnt += 1

    print(f'#{testcase} {cnt}')
