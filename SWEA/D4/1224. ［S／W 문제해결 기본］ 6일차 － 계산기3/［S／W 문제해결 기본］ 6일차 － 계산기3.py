T = 10

operator = {
    '+': lambda x, y: x+y,
    '*': lambda x, y: x*y,
}


def alter_postfix(form):
    postfix = ''
    op_stack = []

    for char in form:
        if char.isdigit():
            postfix += char
        else:
            # 괄호가 존재할 때,
            if '(' in op_stack:
                # 원래 로직과 동일(*가 +보다 우선순위가 높으므로)
                if char == '+':
                    while op_stack[-1] != '(':
                        postfix += op_stack.pop()
                    op_stack.append(char)
                elif char == '*' or char == '(':
                    op_stack.append(char)
                # 닫힌 괄호를 만나면, 열린 괄호 짝까지 계산식에 넣어줌
                elif char == ')':
                    while op_stack[-1] != '(':
                        postfix += op_stack.pop()
                    # 열린 괄호는 따로 없애주기
                    op_stack.pop()
            else:
                # *가 +보다 우선순위 높음
                if char == '+':
                    while op_stack:
                        postfix += op_stack.pop()
                    op_stack.append(char)
                if char == '*' or char == '(':
                    op_stack.append(char)

    while op_stack:
        postfix += op_stack.pop()

    return postfix


def cal_postfix(postfix):
    cal_stack = []

    for char in postfix:
        if char.isdigit():
            cal_stack.append(int(char))
        else:
            b = cal_stack.pop()
            a = cal_stack.pop()
            cal_stack.append(operator[char](a, b))

    return cal_stack[-1]


for testcase in range(1, T+1):
    n = int(input())
    form = list(input())
    print(f'#{testcase} {cal_postfix(alter_postfix(form))}')
