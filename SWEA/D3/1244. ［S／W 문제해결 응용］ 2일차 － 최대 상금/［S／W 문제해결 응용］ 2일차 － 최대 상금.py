T = int(input())

def back_tracking(k=0):
    global max_num

    if k == cnt:
        max_num = max(max_num, int(''.join(list_num)))
        return

    for i in range(N - 1):
        for j in range(i+1, N):
            list_num[i], list_num[j] = list_num[j], list_num[i]
            current_num = int(''.join(list_num))

            if (k, current_num) not in duplicate:
                back_tracking(k + 1)
                duplicate.add((k, current_num))

            list_num[i], list_num[j] = list_num[j], list_num[i]

for testcase in range(1, T+1):
    num, cnt = map(int, input().split())
    list_num = list(str(num))
    N = len(list_num)
    max_num = 0

    duplicate = set()

    # cnt가 0이거나 모든 숫자가 같은 경우를 처리
    if cnt == 0 or len(set(list_num)) == 1:
        print(f'#{testcase} {num}')
    else:
        back_tracking()
        print(f'#{testcase} {max_num}')