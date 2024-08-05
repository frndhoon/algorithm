T = 10
matrix_len = 8


def find_palindrome(matrix):
    cnt = 0

    for item in matrix:
        # 탐색 범위 설정
        for idx in range(matrix_len - target_len + 1):
            # 탐색 부분문자열 설정
            sub_string = item[idx:idx+target_len]
            
            # 부분문자열 범위
            for i in range(target_len // 2):
                # 앞뒤 비교
                if sub_string[i] != sub_string[-i-1]:
                    break
            else:
                cnt += 1

    return cnt


for testcase in range(1, T+1):
    target_len = int(input())

    matrix = [list(input()) for _ in range(matrix_len)]
    matrix_90 = zip(*matrix[::-1])

    palindrome_cnt = find_palindrome(matrix) + find_palindrome(matrix_90)

    print(f'#{testcase} {palindrome_cnt}')
