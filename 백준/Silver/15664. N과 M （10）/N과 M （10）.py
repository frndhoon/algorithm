n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

def back_tracking(lst, idx=0):
    if len(lst) == m:
        print(*lst)
        return

    remember = 0
    for i in range(idx, n):
        if remember != num_list[i]:
            remember = num_list[i]
            lst.append(num_list[i])
            back_tracking(lst, i+1)
            lst.pop()

back_tracking([])