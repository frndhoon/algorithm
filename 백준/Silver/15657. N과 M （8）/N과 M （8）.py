n, m = map(int, input().split())

num_list = sorted(list(map(int, input().split())))


def back_tracking(lst, before_num):
    if len(lst) == m:
        print(*lst)
        return

    for num in num_list:
        if num >= before_num:
            lst.append(num)
            back_tracking(lst, num)
            lst.pop()


back_tracking([], num_list[0])

