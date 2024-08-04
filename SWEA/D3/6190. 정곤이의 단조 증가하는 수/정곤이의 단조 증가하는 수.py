T = int(input())

# 버블 정렬
def bubble_sort(lst):
    length = len(lst)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


# 선택 정렬
def judge_danjo(num):
    num = str(num)
    length = len(num)

    for idx in range(length):
        min_index = idx
        for j in range(idx + 1, length):
            if num[min_index] > num[j]:
                return False

    return True

for testcase in range(1, T+1):
    num = int(input())
    num_list = list(map(int, input().split()))
    bubble_sort(num_list)

    # 단조 수를 비교할 리스트 (Ai x Aj)
    danjo = []
    for i in range(len(num_list) - 1):
        for j in range(i+1, len(num_list)):
            danjo.append(num_list[i] * num_list[j])
            
    # 증가하는 수가 없다면 -1 출력
    max_danjo = -1

    for num in danjo:
        # 단조 수면서 최댓값 출력
        if judge_danjo(num) and num > max_danjo:
            max_danjo = num

    print(f'#{testcase} {max_danjo}')