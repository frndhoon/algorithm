# [1] N // 4씩 나눠서 비밀번호 해제(set)에 담기
def divide_box_to_password(box):
    for i in range(0, box_len, password_len):
        set_password.add(''.join(box[i:i+password_len]))

T = int(input())

for testcase in range(1, T+1):
    # N: 숫자의 개수, K: 크기 순서(목표)
    box_len, target_order = map(int, input().split())
    password_len = box_len // 4  # 패스워드는 4변으로 나눠짐

    box = list(input())

    set_password = set()

    # [1] N // 4씩 나눠서 비밀번호 해제(set)에 담기
    divide_box_to_password(box)

    # [2] 회전하기
    for _ in range(password_len):  # 비밀번호 길이만큼 회전하면 똑같아짐
        box = [box[-1]] + box[:box_len-1]
        divide_box_to_password(box)

    list_password = []
    # [3] 비밀번호 해제에 담긴 16진수를 10진수로 변경하기
    for password in set_password:
        list_password.append(int(password, 16))

    # [4] list로 바꾸고 내림차순 정렬
    list_password.sort(reverse=True)

    # [5] K번째 수 뽑기
    print(f'#{testcase} {list_password[target_order-1]}')
