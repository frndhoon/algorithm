T = int(input())
max_num = 12
target_set = [i for i in range(1, max_num + 1)]

for testcase in range(1, T+1):
    n, k = map(int, input().split())
    cnt = 0

    for i in range(1 << max_num): # 부분집합 개수만큼 반복 (2^12 = 4096 => 비트로는 000000000000 ~ 111111111111까지)
        part_set = [] # 부분집합 저장 및 초기화

        for j in range(max_num): # 12개의 각 원소 각각에 대해
            if i & (1 << j): # i의 j번째 비트가 1인지 확인
                part_set.append(target_set[j]) # 비트가 1인 경우 해당 원소 추가

        if len(part_set) == n and sum(part_set) == k:
            cnt += 1
    print(f'#{testcase} {cnt}')

