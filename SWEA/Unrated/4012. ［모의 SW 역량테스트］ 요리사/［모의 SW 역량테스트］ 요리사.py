# [1] 음식 맛 계산하기
def calculate_flavor_difference(group, matrix):
    total = 0
    for i in group:
        for j in group:
            if i != j:
                total += matrix[i][j]
    return total

# [2] 음식 두 분류로 나누기
def divide_food(idx, set_a, set_b):
    global min_difference

    if idx == N:
        if len(set_a) >= 2 and len(set_b) >= 2:
            diff_a = calculate_flavor_difference(set_a, matrix)
            diff_b = calculate_flavor_difference(set_b, matrix)
            min_difference = min(min_difference, abs(diff_a - diff_b))
        return

    set_a_copy = set_a.copy()
    set_a_copy.add(idx)
    divide_food(idx + 1, set_a_copy, set_b)

    set_b_copy = set_b.copy()
    set_b_copy.add(idx)
    divide_food(idx + 1, set_a, set_b_copy)


T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_difference = float('inf')
    divide_food(0, set(), set())

    print(f"#{testcase} {min_difference}")