n, m = map(int, input().split())
visited = [False] * (n + 1)


def back_tracking(result):
    if len(result) == m:
        print(*result)
        return

    for num in range(1, n+1):
        if not visited[num]:
            visited[num] = True
            result.append(num)
            back_tracking(result)
            result.pop()
            visited[num] = False


back_tracking([])
