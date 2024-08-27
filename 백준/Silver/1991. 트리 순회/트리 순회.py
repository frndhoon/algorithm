# 1 <= N <= 26 노드의 개수

tree = {}
left = {}
right = {}

# [1] 순회
def get_traversal_result(mode, node='A'):
    global result

    if mode == 'preorder':
        result[mode] += tree[node]

    # [2] 왼쪽이 있니?
    if left[node] != '.':
        get_traversal_result(mode, left[node])

    if mode == 'inorder':
        result[mode] += tree[node]

    # [3] 오른쪽이 있니?
    if right[node] != '.':
        get_traversal_result(mode, right[node])

    if mode == 'postorder':
        result[mode] += tree[node]

N = int(input())  # 이진 트리의 노드 개수

for i in range(N):
    pv, lv, rv = input().split()  # 부모 노드, 왼쪽 자식 노드, 오른쪽 자식 노드
    tree[pv] = pv
    left[pv] = lv
    right[pv] = rv

result = {
    'preorder': '',
    'inorder': '',
    'postorder': '',
}

get_traversal_result('preorder')
get_traversal_result('inorder')
get_traversal_result('postorder')

print(*result.values(), sep='\n')
