# 2초, 2억번
T = int(input())
result_list = []

for testcase in range(1, T+1):
    # A~B, C~D
    A, B, C, D = map(int, input().split())

    # 나중에 켜진 전구 시간 시작점
    start = max(A, C)
    # 먼저 꺼진 전구 시간이 끝점
    end = min(B, D)


    result = end - start
    if result <= 0:  # 시간이 안 겹치는 경우
        result = 0

    result_list.append(result)


for testcase, result in enumerate(result_list, start=1):
    print(f'#{testcase} {result}')