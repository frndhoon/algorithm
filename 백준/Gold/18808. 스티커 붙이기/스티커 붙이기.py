# 세로, 가로, 스티커의 수
N, M, K = map(int, input().split())

card_list = []
for _ in range(K):
    R, C = map(int, input().split())
    card_list.append([list(map(int, input().split())) for _ in range(R)])


# [1] 카드 회전 (시계방향으로 90도씩)
def rotate(card):
    return list(map(list, zip(*card[::-1])))


# [2] 노트북에 붙인 카드 얻기
def get_card_to_notebook():
    notebook = [[0 for _ in range(M)] for _ in range(N)]

    for card in card_list:
        is_attached = False  # 붙였는지 확인
        for _ in range(4): # 최대 4번 회전
            if is_attached:
                break
            for i in range(N - len(card) + 1):
                if is_attached:
                    break
                for j in range(M - len(card[0]) + 1):
                    if can_attach(i, j, card, notebook):
                        attach_card(i, j, card, notebook)
                        is_attached = True
                        break
            if not is_attached:
                card = rotate(card)

    return notebook

# [3] 붙일 수 있는지 확인
def can_attach(x, y, card, notebook):
    for i in range(len(card)):
        for j in range(len(card[0])):
            if card[i][j] == 1:
                if x+i >= N or y+j >= M or notebook[x+i][y+j] == 1:
                    return False
    return True


# [4] 카드 붙이기
def attach_card(x, y, card, notebook):
    for i in range(len(card)):
        for j in range(len(card[0])):
            if card[i][j] == 1:
                notebook[x+i][y+j] = 1


# [5] 스티커가 붙은 칸의 수 세기
def count_card_cnt(notebook):
    card_cnt = 0

    for col in range(N):
        for row in range(M):
            if notebook[col][row] == 1:
                card_cnt += 1

    return card_cnt

notebook = get_card_to_notebook()
result = count_card_cnt(notebook)
print(result)