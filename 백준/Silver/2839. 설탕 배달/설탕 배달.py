sugar = int(input())

cnt = 0

while sugar >= 0:
    # 5로 나누어 떨어지면, 바로 봉지 포장
    if sugar % 5 == 0:
        cnt += sugar // 5
        print(cnt)
        break

    # 아니면 3씩 포장
    else:
        sugar -= 3
        cnt += 1

else:
    print(-1)
