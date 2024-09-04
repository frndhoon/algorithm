def find_runway(cliffs):
    runway_cnt = 0

    for cliff in cliffs:
        current_height = cliff[0]  # 현재 높이
        current_length = 1  # 현재 길이 (1로 시작)

        for i in range(1, len(cliff)):
            next_height = cliff[i]

            if current_height == next_height:
                current_length += 1
            else:  # 현재 높이와 다음 높이가 다르다면,
                if abs(current_height - next_height) > 1:
                    break

                if next_height > current_height:  # 오르막
                    if current_length < length:  # 현재 길이가 충분치 않으면 종료
                        break
                    current_length = 1  # 아니라면 길이 초기화
                else:  # 내리막
                    if i + length > len(cliff):
                        break  # 내리막을 놓기 위한 공간이 부족하면 종료
                    if any(h != next_height for h in cliff[i:i + length]):  # any = iterable 객체 중 하나라도 True면 True
                        break  # 내리막을 놓을 구간의 높이가 일정하지 않으면 종료

                    # 내리막을 설치하면 그 구간이 끝날 때까지 다른 활주로를 설치할 수 없음 (음수로 설정)
                    current_length = -length + 1

                current_height = next_height

        else:
            runway_cnt += 1

    return runway_cnt


T = int(input())
for testcase in range(1, T + 1):
    N, length = map(int, input().split())

    cliffs = [list(map(int, input().split())) for _ in range(N)]
    rotate_cliffs = list(map(list, zip(*cliffs)))

    runway_cnt = 0  # 활주로 개수

    runway_cnt += find_runway(cliffs)
    runway_cnt += find_runway(rotate_cliffs)

    print(f'#{testcase} {runway_cnt}')
