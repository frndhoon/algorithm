T = int(input())
for testcase in range(1, T + 1):

    A, B, C = map(int, input().split())  # 3개 박스만 들어옴

    cnt = 0

    if B < 2 or C < 3:
        print(f'#{testcase} -1')
        continue

    if C <= B:
        while C <= B:
            B -= 1
            cnt += 1

    if B <= A:
        while B <= A:
            A -= 1
            cnt += 1

    print(f'#{testcase} {cnt}')