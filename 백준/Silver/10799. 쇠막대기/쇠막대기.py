sliver_rod = list(input())
cnt = 0
stack = []

for idx in range(len(sliver_rod)):
    # 열렸으면 막대 만들기
    if sliver_rod[idx] == '(':
        stack.append(sliver_rod[idx])

    # 닫혔으면 레이저 or 막대 끝
    elif sliver_rod[idx] == ')':
        stack.pop()
        recent_rod = sliver_rod[idx - 1]

        # 연속됐으면 레이저로 열린 막대 수만큼 카운트
        if recent_rod == '(':
            cnt += len(stack)
        # 아니라면 막대 마지막 조각 카운트
        elif recent_rod == ')':
            cnt += 1

print(cnt)
