from collections import deque
A, B = map(int, input().split())


def get_min_calculation_count(start, end):
    """
    start에서 end로 바꾸는데 필요한 연산의 최솟값 구하기(bfs)
    :param start: 시작 숫자
    :param end: 목표 숫자
    :return: 연산 최솟값
    """

    # 처음 숫자, 연산 횟수
    queue = deque([(start, 0)])

    while queue:
        current_num, current_cnt = queue.popleft()

        if current_num == end:
            # 최솟값에 1을 더한 값을 출력한다.
            return current_cnt + 1

        # 2를 곱하거나, 1을 수의 가장 오른쪽에 추가해야함.
        for next_num in (current_num * 2, int(str(current_num) + '1')):
            if next_num <= 0 or next_num >= 10e9: continue
            queue.append((next_num, current_cnt + 1))

    return -1


result = get_min_calculation_count(A, B)
print(result)