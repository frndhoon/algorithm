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
            if not op_stack:
                op_stack.append(char)
            else:
                if char == '+':
                    while op_stack:
                        postfix += op_stack.pop()
                    op_stack.append(char)
                elif char == '*':
                    op_stack.append(char)

    while op_stack:
        postfix += op_stack.pop()

    return postfix


def calculate_postfix(postfix):
    cal_stack = []
    for char in postfix:
        if char.isdigit():
            cal_stack.append(char)
        else:
            b = int(cal_stack.pop())
            a = int(cal_stack.pop())
            cal_stack.append(operator[char](a, b))

    return cal_stack[-1]


for testcase in range(1, T + 1):
    n = int(input())
    form = input()

    print(f'#{testcase} {calculate_postfix(alter_postfix(form))}')
