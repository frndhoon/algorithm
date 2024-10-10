def solve(num, cnt):
    """

    :param num: 자연수 A
    :param cnt: B번 곱하는 횟수
    :return:
    """
    if cnt == 1:  # 1 제곱이면, 나눈 나머지 반환
        return num % C
    else:
        tmp = solve(num, cnt//2)
        if cnt % 2 == 0 : # 짝수인 경우
            return (tmp * tmp) % C
        else: # 홀수인 경우
            return (tmp * tmp * num) % C


A, B, C = map(int, input().split())

result = solve(A, B)
print(result)