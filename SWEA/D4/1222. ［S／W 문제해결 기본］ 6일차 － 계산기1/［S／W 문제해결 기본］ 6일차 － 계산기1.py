T = 10
 
 
def infix_to_postfix(form):
    # 후위 표기식 변환 결과를 저장할 리스트
    postfix = []
    # 연산자를 저장할 스택
    stack = []
 
    for char in form:
        # 숫자면 후위 표기식에 저장
        if char.isdigit():
            postfix.append(char)
        # +일 경우, 연산자 스택에 있는 연산자를 모두 후위 표기식에 저장
        elif char == '+':
            while stack:
                postfix.append(stack.pop())
            stack.append(char)
 
    if stack:
        postfix.append(stack.pop())
 
    return ''.join(postfix)
 
 
def calculate_postfix(form):
    stack = []
 
    for char in form:
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 + num2)
 
    return stack[0]
 
 
for testcase in range(1, T + 1):
    n = int(input())
    form = input()
 
    postfix_form = infix_to_postfix(form)
 
    result = calculate_postfix(postfix_form)
 
    # 결과 출력
    print(f"#{testcase} {result}")