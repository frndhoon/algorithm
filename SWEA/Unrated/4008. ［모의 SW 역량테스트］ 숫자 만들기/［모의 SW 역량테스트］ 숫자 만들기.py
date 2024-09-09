plus, minus, multiply, divide = 0, 1, 2, 3

def calculate(num1, num2, operator):
    if operator == plus:
        return num1 + num2
    elif operator == minus:
        return num1 - num2
    elif operator == multiply:
        return num1 * num2
    elif operator == divide:
        return num1 // num2 if num1 >= 0 else -(abs(num1) // num2)

def dfs(depth, total):
    global max_answer, min_answer

    if depth == N:
        min_answer = min(min_answer, total)
        max_answer = max(max_answer, total)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            dfs(depth + 1, calculate(total, numbers[depth], i))
            operators[i] += 1


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_answer = float('-inf')
    min_answer = float('inf')

    dfs(1, numbers[0])

    result = max_answer - min_answer

    print(f'#{testcase} {result}')