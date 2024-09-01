# [1] 16진수 -> 2진수
def change_hexa_to_binary(hexa_num):
    binary_num = ''
    for h in hexa_num:
        if h.isdigit():
            binary_num += change_dec_to_binary(int(h))
        else:
            binary_num += change_dec_to_binary(ord(h) - 55)

    return binary_num

# [2] 10진수 -> 4자리 2진수
def change_dec_to_binary(decimal_num):
    binary_num = ''
    for i in range(4):
        binary_num += str(decimal_num % 2)
        decimal_num //= 2

    return binary_num[::-1]

T = int(input())

for testcase in range(1, T+1):
    N, hexa_num = input().split()
    N = int(N)

    result = change_hexa_to_binary(hexa_num)
    
    print(f'#{testcase} {result}')

