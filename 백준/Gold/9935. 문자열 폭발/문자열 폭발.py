char_list = list(input())
explore_char = input()

stack = []

for char in char_list:
    stack.append(char)
    # 스택 마지막이 폭발 문자열이 맞는지 탐색
    target_char = ''.join(map(str, stack[len(stack)-len(explore_char):len(stack)]))
    if target_char == explore_char:
        for _ in range(len(explore_char)):  # 맞다면, 그만큼 stack에서 pop해주기
            stack.pop()

result = ''.join(map(str, stack))
print(result if result else "FRULA")
