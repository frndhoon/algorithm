T = 10


def get_min_max_idx(lst):

    min_idx = max_idx = 0
    # 최소값 인덱스, 최대값 인덱스 구하기
    for idx in range(1, len(lst)):
        if lst[idx] < lst[min_idx]:
            min_idx = idx
        elif lst[idx] > lst[max_idx]:
            max_idx = idx

    return min_idx, max_idx


for testcase in range(1, T+1):
    dump_cnt = int(input())
    box_list = list(map(int, input().split()))

    # 덤프 수행 횟수만큼 시행
    for _ in range(dump_cnt):
        min_height_idx, max_height_idx = get_min_max_idx(box_list)
        box_list[min_height_idx] += 1
        box_list[max_height_idx] -= 1

    min_height_idx, max_height_idx = get_min_max_idx(box_list)
    height_diff = box_list[max_height_idx] - box_list[min_height_idx]
    print(f'#{testcase} {height_diff}')
