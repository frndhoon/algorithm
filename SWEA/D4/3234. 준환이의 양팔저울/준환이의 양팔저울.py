# 1 <= N <= 9
# 백트래킹

# 팩토리얼
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def backtracking(left_scale=0, right_scale=0, cnt=0):
    global answer

    # [1] 왼쪽, 오른쪽의 저울에 N이 다 올려져있는가 판단
    if cnt == N:
        answer += 1  # [2] 방법 수 카운팅
        return

    if left_scale > sum_weight // 2: # [+] 왼쪽 저울에 이미 전체 무게의 절반 이상이 들어갔으면,
        answer += 2 ** (N - cnt) * factorial(N - cnt)  # 무게추가 왼쪽, 오른쪽 올라가는지(2의 (N-cnt)승) / 순서를 고려해서 (N-cnt)!
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            backtracking(left_scale + weight_list[i], right_scale, cnt + 1)

            # [3] 왼쪽 저울 >= 오른쪽 저울인지 판단
            if left_scale >= right_scale + weight_list[i]:
                backtracking(left_scale, right_scale + weight_list[i], cnt + 1)

            used[i] = False

# [result] 양팔 저울에 모든 무게추를 올리는 방법 출력
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    answer = 0
    weight_list = list(map(int, input().split()))
    sum_weight = sum(weight_list)
    used = [False] * (N)  # 무게추 사용 판단

    backtracking()
    print(f'#{testcase} {answer}')