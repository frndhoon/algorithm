# [1] 음식 맛 계산하기
def calculate_flavor_difference(food_a, food_b):
    global min_difference
    a_sum, b_sum = 0, 0
    for i in range(N // 2):  # 반반이므로 반만 탐색하면 됨
        for j in range(N // 2):
            a_sum += matrix[food_a[i]][food_a[j]]
            b_sum += matrix[food_b[i]][food_b[j]]
    min_difference = min(min_difference, abs(a_sum - b_sum))

# [2] 음식 두 분류로 나누기
def divide_food(food_a, food_b, cnt=0):
    global min_difference
    if cnt == N:
        if len(food_a) == N // 2:  # N / 2씩 나누어지면 계싼
            calculate_flavor_difference(food_a, food_b)
        return

    divide_food(food_a + [cnt], food_b, cnt+1)  # a에 넣기
    divide_food(food_a, food_b + [cnt], cnt+1)  # b에 넣기

T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_difference = float('inf')
    divide_food([], [])

    print(f"#{testcase} {min_difference}")