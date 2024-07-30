T = 10


# list안의 수 중 max 수를 찾는 함수
def get_maximum(target_building_list):
    
    # 초기 max값은 첫번째 idx값
    max_num = target_building_list[0]
    for num in target_building_list[1:]:
        if num > max_num:
            max_num = num
    return max_num


for testcase in range(1, T + 1):
    n = int(input())
    building_list = list(map(int, input().split()))
    count = 0

    # 양 옆 두 칸씩 높이가 0인 건물이 있으므로 2, n - 2까지 탐색
    for idx in range(2, n - 2):

        # 현재 building의 높이
        current_building = building_list[idx]

        # 현재 building 양 옆 2개씩, 총 4개의 건물 높이 중 가장 큰 높이
        max_around_building = get_maximum(building_list[idx - 2:idx] + building_list[idx + 1:idx + 3])

        # 만약 현재 높이가 양 옆 2개씩, 총 4개의 건물 높이 중 가장 큰 높이보다 크다면,
        if current_building > max_around_building:
            # 현재 높이에서 가장 큰 높이를 뺀 값을 세대 수에 더하기
            # 양쪽 모두 거리 2 이상의 공간이 확보돼야하므로 주위 세대 중 가장 큰 높이만 빼면 됨
            count += current_building - max_around_building

    print(f'#{testcase} {count}')
