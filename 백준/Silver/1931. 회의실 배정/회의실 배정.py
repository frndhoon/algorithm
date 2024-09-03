N = int(input())  # 회의의 수
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x:(x[1], x[0]))


meeting_idx = 0
meeting_cnt = 1

current_end = meetings[0][1]

for idx in range(1, N):
    next_start = meetings[idx][0]
    next_end = meetings[idx][1]
    if current_end <= next_start:
        current_end = next_end  # 다음 회의실로
        meeting_cnt += 1  # 회의실 개수 +1

print(meeting_cnt)