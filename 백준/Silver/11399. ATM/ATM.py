import sys

input = sys.stdin.readline

n = int(input())
people = sorted(list(map(int, input().split())))
total_wating_time = 0
current_time = 0

for time in people:
    current_time += time
    total_wating_time += current_time

print(total_wating_time)
