from collections import deque

T = 10

for _ in range(T):
    testcase = int(input())
    num_list = deque(list(map(int, input().split())))
    cycle = [1, 2, 3, 4, 5]
    idx = 0

    while num_list[-1] > 0:
        num_list.append(num_list.popleft() - cycle[idx % 5])
        idx += 1

    num_list[-1] = 0

    print(f"#{testcase} {' '.join(map(str, num_list))}")
