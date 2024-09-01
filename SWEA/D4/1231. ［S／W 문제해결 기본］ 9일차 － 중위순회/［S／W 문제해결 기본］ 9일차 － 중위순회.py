def read_inorder(node):
    global answer

    if node <= N:
        if left_child[node]:
            read_inorder(node * 2)  # 왼쪽 자식 노드

        answer += tree[node]

        if right_child[node]:
            read_inorder(node * 2 + 1)  # 오른쪽 자식 노드


T = 10

for testcase in range(1, T+1):
    answer = ''  # 문자를 저장할 string

    N = int(input())  # 정점의 총 수

    tree = [0] * (N+1)
    left_child = [0] * (N+1)
    right_child = [0] * (N+1)


    for _ in range(N):
        node, data, *child = input().split()
        node = int(node)
        tree[node] = data
        if len(child) == 2:
            left_child[node] = int(child[0])
            right_child[node] = int(child[1])
        elif len(child) == 1:
            left_child[node] = int(child[0])

    read_inorder(1)

    print(f'#{testcase} {answer}')