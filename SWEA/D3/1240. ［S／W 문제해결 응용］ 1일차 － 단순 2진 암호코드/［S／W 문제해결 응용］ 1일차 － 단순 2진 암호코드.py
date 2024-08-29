CODE_TO_NUMBER = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9',
}


# [1] 암호 탐색
def find_password(matrix):
    # 암호 탐색
    for row in range(N):
        for col in range(M - 1, -1, -1):
            if matrix[row][col] == '1':  # 암호 시작 찾으면 (뒤에서부터 찾아야 암호 찾을 수 있음) => 맨뒤 숫자 1로 시작함
                return change_password(''.join(matrix[row][col - 55:col + 1]))


# [2] 암호코드 변환
def change_password(code):
    password = ''
    # 7자리씩 끊기
    for i in range(0, len(code)-6, 7):
        password += CODE_TO_NUMBER[code[i:i+7]]

    return password

# [3] 암호 계산
def calculate_password(password):
    odd_sum, even_sum = 0, 0

    for i in range(0, len(password), 2):
        odd_sum += int(password[i])
        even_sum += int(password[i+1])

    return odd_sum, even_sum


# [4] 암호 코드 판단
def judge_password(odd_sum, even_sum):
    if ((odd_sum * 3) + even_sum) % 10 == 0:
        return True
    return False


T = int(input())
for testcase in range(1, T+1):
    # N = row, M = col
    N, M = map(int, input().split())

    matrix = [list(input()) for _ in range(N)]

    password = find_password(matrix)
    odd_sum, even_sum = calculate_password(password)  # 홀수 합, 짝수 합 구하기
    
    result = 0  # 잘못된 암호코드일 경우 0 출력 (기본값)
    
    # [result] 검증코드가 맞으면, 포함된 숫자의 합을 출력
    if judge_password(odd_sum, even_sum):
        result = odd_sum + even_sum

    print(f'#{testcase} {result}')
