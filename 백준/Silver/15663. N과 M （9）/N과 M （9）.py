n, m = map(int, input().split())

num_list = sorted(list(map(int, input().split())))
visited = [False] * n

def back_tracking(lst):
    if len(lst) == m:
        print(*lst)
        return

    # 바로 전 것과 숫자 비교
    remember = 0
    for i in range(len(num_list)):
        if not visited[i] and remember != num_list[i]:
            remember = num_list[i]
            lst.append(num_list[i])
            visited[i] = True
            back_tracking(lst)
            lst.pop()
            visited[i] = False

back_tracking([])