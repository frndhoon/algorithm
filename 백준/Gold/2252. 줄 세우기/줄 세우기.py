from collections import deque
student_cnt, compare_cnt = map(int, input().split())

# 모든 노드 진입차수(indegree) 0으로 초기화
indegrees = [0] * (student_cnt+1)
graph = [[] for _ in range(student_cnt+1)]

for _ in range(compare_cnt):
    front, back = map(int, input().split())
    graph[front].append(back)
    # 진입차수 증가
    indegrees[back] += 1

def topo_sort():
    """
    위상 정렬
    :return: 
    """
    result = []
    queue = deque()

    for i in range(1, student_cnt+1):
        # 진입차수 0인 것만 큐에 넣기
        if indegrees[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        for i in graph[current]:
            # 방문했으니까 해당 노드에서 나가는 간선을 그래프에서 제거
            indegrees[i] -= 1
            # 새롭게 진입차수가 0이면 큐에 넣기
            if indegrees[i] == 0:
                queue.append(i)

    return result

answer = topo_sort()
print(*answer, sep=' ')