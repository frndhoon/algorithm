# [1] 교환 횟수만큼 교환했을 때, 최대값 비교
def solve(cnt, num_list):
    global max_num

    if cnt == int(change_cnt):
        max_num = max(max_num, int(''.join(num_list)))
        return

    for i in range(len(num) - 1):
        for j in range(i+1, len(num)):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            current_num = ''.join(num_list)

            if (cnt, current_num) not in visited:  # [2] 교환했을 때, 이미 비교된 값이라면 비교하지말기
                visited.add((cnt, current_num))
                solve(cnt+1, num_list)

            num_list[i], num_list[j] = num_list[j], num_list[i]

T = int(input())

for testcase in range(1, T+1):
    max_num = 0

    num, change_cnt = input().split()
    num_list = list(num)

    visited = set()  # (횟수, 숫자)

    solve(0, num_list)

    print(f'#{testcase} {max_num}')
