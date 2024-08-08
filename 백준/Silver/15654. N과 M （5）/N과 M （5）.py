n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

def back_tracking(lst):
    length = len(lst)
    if length == m:
        print(*lst)
        return
    for num in num_list:
        if num not in lst:
            lst.append(num)
            back_tracking(lst)
            lst.pop()


back_tracking([])
