n = int(input())
form = list(input())
operator = {'+': lambda x,y: int(x)+int(y),
            '-': lambda x,y: int(x)-int(y),
            '*': lambda x,y: int(x)*int(y)}
max_sum = -(2**31)


def bracket_calculate(idx=0, value=int(form[0])):
    global max_sum
    if idx == n - 1:
        max_sum = max(max_sum, value)
        return

    # 다음거부터 괄호 씌워서 계산
    if idx + 2 < n:
        next_value = operator[form[idx+1]](value, form[idx+2])
        bracket_calculate(idx + 2, next_value)

    # 다음 다음거부터 괄호 씌워서 계산
    if idx + 4 < n:
        next_next_value = operator[form[idx+3]](form[idx+2], form[idx+4])
        next_value = operator[form[idx+1]](value, next_next_value)
        bracket_calculate(idx + 4, next_value)

bracket_calculate()
print(max_sum)
