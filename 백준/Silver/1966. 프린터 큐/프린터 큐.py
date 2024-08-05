T = int(input())

for _ in range(T):
    length, wonder_idx = map(int, input().split())

    # (idx, value) 형태인 tuple을 저장할 프린터 큐
    print_queue = []
    queue = []

    for idx, value in enumerate(map(int, input().split())):
        queue.append((value, idx))
    idx = 0
    while queue:

        # FIFO
        wonder_doc = queue.pop(0)
        
        # 우선순위 높은 게 있다면, Queue의 가장 뒤에 재배치
        if queue and wonder_doc[0] < max(queue, key=lambda x: x[0])[0]:
            queue.append(wonder_doc)
        
        # 아니면 바로 인쇄
        else:
            idx += 1
            print_queue.append((idx, wonder_doc))

    for item in print_queue:
        wonder = item[1][1]
        if wonder == wonder_idx:
            print(item[0])
            break
