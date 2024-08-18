from collections import deque
T = int(input())


# 16진수니 4를 나눈 만큼 반복
def rotate_password(lst):
    dq = deque(lst)
    for _ in range(N//4):
        dq.appendleft(dq.pop())
        get_password(dq)


# 16진수만큼 쪼개서 리스트로 만들기
def get_password(dq):
    password_list = []
    char = ''.join(list(dq))
    for idx in range(0, N, N//4):
        password_list.append(char[idx:idx+N//4])

    change_10_digits(password_list)


# 16진수 -> 10진수
def change_10_digits(lst):
    global duplicate

    for password in lst:
        duplicate.add(int(password, 16))


for testcase in range(1, T+1):
    # N: 4의 배수, 숫자 개수
    # K: K번째로 큰 수(내림차순 정렬 시)
    N, K = map(int, input().split())
    password_16_digits = list(input())

    duplicate = set()

    rotate_password(password_16_digits)
    result = sorted(list(duplicate), reverse=True)

    print(f'#{testcase} {result[K-1]}')

