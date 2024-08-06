n, m = map(int, input().split())


def back_tracking(data):
    length = len(data)
    if length == m:
        print(*data, sep=' ')
        return

    for i in range(1, n + 1):
        data.append(i)
        back_tracking(data)
        data.pop()


back_tracking([])
