testcase = int(input())
for _ in range(testcase):
    perform_def_list = input()
    arr_num = int(input())

    # arr을 string으로 줘야하기 때문에 arr의 크기에 따라 arr을 다르게 할당해줌
    if arr_num > 1:
        arr = list(map(int, input().strip('[]').split(',')))
    elif arr_num == 1:
        arr = [int(input().strip('[]'))]
    elif arr_num == 0:
        input()
        arr = []

    # error를 판별하는 변수
    is_error = False
    is_reversed = False

    # 수행함수 하나씩
    for perform_def in perform_def_list:
        
        # R이면 뒤집기
        if perform_def == 'R':
            is_reversed = not is_reversed
        
        # D면 첫 번째 수 버리기
        elif perform_def == 'D':
            if not arr:
                is_error = True
                break
            elif arr:
                if is_reversed:
                    arr.pop()
                else:
                    arr.pop(0)

    if is_error:
        print('error')
    else:
        if is_reversed:
            arr.reverse()
        print(f"[{','.join(list(map(str, arr)))}]")
