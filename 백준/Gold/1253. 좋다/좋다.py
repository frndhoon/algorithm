N = int(input())
lst = list(map(int, input().split()))
lst.sort()  # 정렬

good_numbers = 0

for i in range(N):
    target_num = lst[i]

    # 투 포인터
    left, right = 0, N - 1

    while left < right:

        current_sum = lst[left] + lst[right]

        # 타겟 숫자를 찾았다면, cnt ++ 하고 중단
        if current_sum == target_num and left != i and right != i:
            good_numbers += 1
            break
        
        # 자기 자신은 좋은 수 만들기에 포함할 수 없음
        
        # 타겟 숫자보다 작거나 왼쪽 포인터가 현재 수의 인덱스와 같으면, 왼쪽 포인터 당기기(숫자 더 늘리기)
        elif current_sum < target_num or left == i:
            left += 1
        # 타겟 숫자보다 크거나 오른쪽 포인터가 현재 수의 인덱스와 같으면, 오른쪽 포인터 당기기(숫자 더 줄이기)
        elif current_sum > target_num or right == i:
            right -= 1

print(good_numbers)