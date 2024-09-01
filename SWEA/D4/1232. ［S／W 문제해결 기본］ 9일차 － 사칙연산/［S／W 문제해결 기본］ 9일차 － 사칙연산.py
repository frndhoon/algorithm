operator = {
    '+': lambda x,y:x+y,
    '-': lambda x,y:x-y,
    '*': lambda x,y:x*y,
    '/': lambda x,y:x//y
}

def calculate_tree(node):
    if len(perfect_tree[node]) == 1:
        return int(perfect_tree[node][0])
    else:
        op, left, right = perfect_tree[node]
        left, right = calculate_tree(int(left)), calculate_tree(int(right))

        return operator[op](left, right)

T = 10

for testcase in range(1, T+1):
    N = int(input())

    perfect_tree = [[] for _ in range(N+1)]

    for _ in range(N):
        node, *data = input().split()
        node = int(node)
        perfect_tree[node].extend(data)

    result = calculate_tree(1)

    print(f'#{testcase} {result}')