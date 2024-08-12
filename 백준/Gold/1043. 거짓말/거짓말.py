n, m = map(int, input().split())

know_truth = list(map(int, input().split()))

is_know_truth = [False for _ in range(n+1)]
parties = []


def get_max_party():
    # 진실을 아무도 모르면 파티 개수만큼
    if know_truth[0] == 0:
        return m

    know_truth_people = know_truth[1:]

    # 진실을 아는 사람들은 먼저 표시
    for man in know_truth_people:
        is_know_truth[man] = True

    # 파티 하나씩 저장
    for _ in range(m):
        party = list(map(int, input().split()))[1:]
        parties.append(party)

    changed = True
    while changed:
        changed = False
        for party in parties:
            for person in party:
                # 진실을 아는 사람이 한 명이라도 있다면
                if is_know_truth[person]:
                    # 파티 멤버 탐색하면서 아는 사람으로 만들기
                    for member in party:
                        if not is_know_truth[member]:
                            is_know_truth[member] = True
                            changed = True
                    break

    lies_possible = 0
    for party in parties:
        truth_known = False
        # 한 명이라도 알면, 그 파티는 이미 과장을 못한다는 뜻
        for person in party:
            if is_know_truth[person]:
                truth_known = True
                break
        # 아는 사람이 한 명이라도 없었다면, 과장된 이야기 할 수 있음
        if not truth_known:
            lies_possible += 1

    return lies_possible


result = get_max_party()
print(result)
