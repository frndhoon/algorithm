import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
result = 0

for coin in coins:
    coin_cnt = k // coin
    if coin_cnt > 0:
        result += coin_cnt
        k %= coin

print(result)

