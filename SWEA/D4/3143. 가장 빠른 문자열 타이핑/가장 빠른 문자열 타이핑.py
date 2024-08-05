T = int(input())

for testcase in range(1, T+1):
    main_string, sub_string = input().split()
    main_length = len(main_string)
    sub_length = len(sub_string)

    idx = 0
    cnt = 0

    while idx < main_length:
        # 서브 문자열을 찾았을 때, 서브 문자열만큼 길이 증가시킴
        # 중복 계산을 피해야함
        if main_string[idx:idx+sub_length] == sub_string:
            cnt += 1
            idx += sub_length
        else:
            idx += 1

    # 최솟값은 주문자열에서 서브 문자열의 타이핑 횟수를 빼고, 서브 문자열의 타이핑 횟수를 더한 값
    min_cnt = main_length - (cnt * sub_length) + cnt

    print(f'#{testcase} {min_cnt}')