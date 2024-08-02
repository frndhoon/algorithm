n, m = map(int, input().split())

result = []


def back_tracking(idx):

    if len(result) == m:
        print(*result)
        return

    for num in range(idx, n + 1):
        if num not in result:
            result.append(num)
            back_tracking(num + 1)
            result.pop()


back_tracking(1)
