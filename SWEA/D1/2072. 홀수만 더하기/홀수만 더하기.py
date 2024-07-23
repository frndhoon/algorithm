n = int(input())

for T in range(1, n+1):
    nums = list(map(int, input().split()))
    result = 0
    for num in nums:
        if num % 2 == 1:
            result += num
    print(f'#{T} {result}')