n, m = map(int, input().split())


def back_tracking(result):
    if len(result) == m:
        print(*result)
        return

    for num in range(1, n+1):
        if num not in result:
            result.append(num)
            back_tracking(result)
            result.pop()


back_tracking([])
