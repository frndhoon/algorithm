n, m = map(int, input().split())


def back_tracking(data, idx):
    length = len(data)

    if length == m:
        print(*data, sep=' ')
        return

    for i in range(idx, n+1):
        data.append(i)
        back_tracking(data, i)
        data.pop()


back_tracking([], 1)


