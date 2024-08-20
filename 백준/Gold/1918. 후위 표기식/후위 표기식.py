def alter_postfix(form):
    postfix = ''
    op_stack = []

    # 연산자 우선순위 정의
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for char in form:
        if char.isalpha():
            postfix += char
        elif char == '(':
            op_stack.append(char)
        elif char == ')':
            while op_stack and op_stack[-1] != '(':
                postfix += op_stack.pop()
            op_stack.pop()  # '(' 제거
        else:  # 연산자 처리
            while (op_stack and op_stack[-1] != '(' and
                   precedence[op_stack[-1]] >= precedence[char]):
                postfix += op_stack.pop()
            op_stack.append(char)

    # 스택에 남아 있는 연산자 모두 pop
    while op_stack:
        postfix += op_stack.pop()

    return postfix


# 입력받아 처리
form = input().strip()
print(alter_postfix(form))
