import heapq
testcase = int(input())

for _ in range(testcase):
    cal = int(input())
    min_heap = []
    max_heap = []

    # 최댓값/최솟값에 이미 체크됐으면 서로 제거해줘야하기 때문에 체크사항
    check = [False] * cal

    for idx in range(cal):
        cmd, num = input().split()

        if cmd == 'I':
            # 오름차순
            heapq.heappush(min_heap, (int(num), idx))
            # 내림차순
            heapq.heappush(max_heap, (-int(num), idx))

        elif cmd == 'D':
            if num == '-1' and min_heap:
                check[heapq.heappop(min_heap)[1]] = True
            elif num == '1' and max_heap:
                check[heapq.heappop(max_heap)[1]] = True

        # 최댓값/최솟값에 이미 체크됐으면 서로 제거해주기
        while max_heap and check[max_heap[0][1]]:
            heapq.heappop(max_heap)
        while min_heap and check[min_heap[0][1]]:
            heapq.heappop(min_heap)

    if max_heap:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
    else:
        print('EMPTY')
