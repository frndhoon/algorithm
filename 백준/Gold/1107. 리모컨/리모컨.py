n = int(input())
m = int(input())

if m == 0:
    buttons = []
else:
    buttons = list(map(int, input().split()))

minimum_cnt = abs(100 - n)

for i in range(1000001):
    num = str(i)

    for j in num:
        if int(j) in buttons:
            break
    else:
        minimum_cnt = min(minimum_cnt, abs(n - i) + len(num))

print(minimum_cnt)