def change_binary(num):
    binary_num = ''
    while num != 1:
        if len(binary_num) == 13:
            return 'overflow'

        num *= 2

        if num > 1:
            binary_num += '1'
            num -= 1
        elif num == 1:
            binary_num += '1'
            break
        elif num < 1:
            binary_num += '0'

    return binary_num

T = int(input())
for testcase in range(1, T+1):
    N = float(input())

    result = change_binary(N)

    print(f'#{testcase} {result}')
