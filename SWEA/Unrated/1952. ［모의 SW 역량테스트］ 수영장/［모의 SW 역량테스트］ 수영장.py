# 3초, 3억번

periods = ['1일', '1달', '3달', '1년']

def dfs(month=0, price=0):
    global min_price
    if month == 12:
        min_price = min(min_price, price)
        return

    # 1일치
    dfs(month+1, price+prices['1일']*days[month])

    # 1달치
    # 그 달에 하루라도 가야만 등록하므로, 하루 이상 가는지 확인
    dfs(month+1, price+prices['1달']*(1 if days[month] > 0 else 0))

    # 3달치
    if month + 3 <= 12:
        # 앞으로 세 달치 동안 하루라도 간다면, 1 곱하기 / 아니라면 0 곱하기(그 기간 내에는 안간다는 거니까)
        dfs(month+3, price+prices['3달']*(1 if any(day > 0 for day in days[month:month+3]) else 0))

    # 1년치
    if month == 0:  # 첫달에만 등록하면 끝
        dfs(month+12, price+prices['1년'])


T = int(input())
for testcase in range(1, T+1):
    min_price = float('inf')
    periods = ['1일', '1달', '3달', '1년']
    # 기간: 가격
    prices = {k: v for k, v in zip(periods, list(map(int, input().split())))}

    # 수영장 가는 일수
    days = list(map(int, input().split()))

    dfs()

    print(f'#{testcase} {min_price}')
