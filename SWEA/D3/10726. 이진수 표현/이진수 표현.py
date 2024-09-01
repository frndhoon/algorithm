T = int(input())

for testcase in range(1, T+1):
    # N : 마지막 N 비트
    # M : 정수
    result = 'ON'
    N, M = map(int, input().split())
    for i in range(N):
        if not (M & (1 << i)):
            result = 'OFF'
            break

    print(f'#{testcase} {result}')