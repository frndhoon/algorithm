n, m = map(int, input().split())


def back_tracking(result):

    if len(result) == m:
        print(*result)

    for num in range(1, n + 1):
        if num not in result:
            if result: # 현재 검사할 list가 있다면,
                if num > result[-1]: # 전 원소랑 비교하기
                    result.append(num)
                    back_tracking(result)
                    result.pop()
            else:
                result.append(num)
                back_tracking(result)
                result.pop()


back_tracking([])
