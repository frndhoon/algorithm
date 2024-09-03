# [1] 조합 찾기
def combination(lst=[], idx=0):
    if len(lst) == N // 2:
        calculate_vector(lst)
        return

    for i in range(idx, N):
        if i in lst:
            continue
        lst.append(i)
        combination(lst, i + 1)
        lst.pop()


# 결과 벡터를 구함 (쌍으로 계산하는 것이 아닌)
def calculate_vector(lst):  # 짝짓기
    global min_magnitude
    vector_sum = [0, 0]
    for i in range(N):
        if i in lst:
            for j in range(2):  # 선택된 건 더하기
                vector_sum[j] += worms[i][j]
        else:
            for j in range(2):  # 선택 안된 건 빼기
                vector_sum[j] -= worms[i][j]

    # │V│=│(x, y)│= x * x + y * y => |(ax-bx, ay-by)|
    magnitude = vector_sum[0] ** 2 + vector_sum[1] ** 2
    min_magnitude = min(min_magnitude, magnitude)


T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    worms = [list(map(int, input().split())) for _ in range(N)]

    min_magnitude = float('inf')
    combination()
    print(f"#{testcase} {min_magnitude}")
