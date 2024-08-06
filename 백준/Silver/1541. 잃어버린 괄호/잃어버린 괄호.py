form = input()
min_sum = 0

# 음수 없으면 다 더해주기
if '-' not in form:
    min_sum += sum(map(int, form.split('+')))

else:
    minus_form = form.split('-')
    # 처음 수는 무조건 양수기 때문에 더해줌
    min_sum += sum(map(int, minus_form[0].split('+')))
    # index 0의 값은 이미 봤기 때문에 나머지 수를 탐색
    for char in minus_form[1:]:
        # +가 있다면, 괄호를 치고 빼줘야함
        if '+' in char:
            min_sum -= sum(map(int, char.split('+')))
        # +가 없더라도, 어차피 마이너스였으므로, 빼줌
        else:
            min_sum -= int(char)

print(min_sum)
