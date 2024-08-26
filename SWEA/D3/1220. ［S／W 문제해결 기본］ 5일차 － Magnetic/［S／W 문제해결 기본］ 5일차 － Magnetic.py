N_POLE = 1
S_POLE = 2
T = 10

# [1] N극 아래에 S극이 몇 개 있는지 셈
def count_deadlock(lst):
    global dead_lock

    is_N_pole = False

    for i in range(len(lst)):
        if lst[i] == N_POLE:
            is_N_pole = True  # [2] N극을 만났을 때,
        elif lst[i] == S_POLE and is_N_pole:  # [3] S극을 만나면 교착상태 ++,  셋 이상의 자성체들이 서로 충돌하여 붙어 있을 경우에도 하나의 교착 상태
            is_N_pole = False
            dead_lock += 1


for testcase in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dead_lock = 0

    for i in range(N):
        count_deadlock([item[i] for item in matrix])

    print(f'#{testcase} {dead_lock}')