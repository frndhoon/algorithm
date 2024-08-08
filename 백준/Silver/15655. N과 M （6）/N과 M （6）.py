n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))


def back_tracking(lst, idx):
    length = len(lst)
    if length == m:
        print(*lst)
        return

    for i in range(idx, len(num_list)):
        if num_list[i] not in lst:
            lst.append(num_list[i])
            back_tracking(lst, i)
            lst.pop()


back_tracking([], 0)
