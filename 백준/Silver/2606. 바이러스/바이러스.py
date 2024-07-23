computer = int(input())
n = int(input())

network = [[] for _ in range(computer + 1)]
# virus 감염 여부 저장
is_virus = [False for _ in range(computer + 1)]

# 시작 끝점으로 network에 서로 연결되는 정보 저장
for _ in range(n):
    start, end = list(map(int, input().split()))

    network[start].append(end)
    network[end].append(start)


# virus 걸리게하는 함수
def get_virus(init_computer):
    # 초기 stack은 초기 컴퓨터의 network 값
    stack = network[init_computer]
    # stack이 없어질 때까지 반복
    while stack:
        # stack의 뒤에서 컴퓨터 번호를 가져옴
        current_computer = stack.pop()
        # virus에 걸리지 않았다면, 감염시키고, 그 컴퓨터에 연결돼있는 컴퓨터 탐색
        if not is_virus[current_computer]:
            is_virus[current_computer] = True
            stack.extend(network[current_computer])


# 1번 컴퓨터가 웜 바이러스에 걸렸을 때
get_virus(1)


# False는 0이고, True는 1
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수(때문에 is_virus False로 초기화)
is_virus[1] = False
print(sum(is_virus))
