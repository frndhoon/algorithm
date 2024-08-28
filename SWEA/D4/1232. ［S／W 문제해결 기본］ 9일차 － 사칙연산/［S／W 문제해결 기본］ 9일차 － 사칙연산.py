OPERATOR = {
    '+': lambda x, y: int(x)+int(y),
    '-': lambda x, y: int(x)-int(y),
    '/': lambda x, y: int(x)//int(y),
    '*': lambda x, y: int(x)*int(y),
}


def calculate(node):
    if len(tree[node]) == 1:  # 숫자 반환
        return int(tree[node][0])

    else:  # 연산해주기
        op, left, right = tree[node]
        left_value, right_value = calculate(int(left)), calculate(int(right))

        return OPERATOR[op](left_value, right_value)

T = 10

for testcase in range(1, T+1):
    N = int(input())  # 정점의 개수
    tree = [[] for _ in range(N + 1)]

    for _ in range(N):
        v, *data = input().split()  # data는 연산자+자식 or 숫자
        v = int(v)
        tree[v].extend(data)

    result = calculate(1)

    print(f'#{testcase} {result}')
