import sys
input = sys.stdin.readline

listen_num, see_num = map(int, input().split())

listen_arr = set([])
see_arr = set([])
listen_see_arr = set([])

for _ in range(listen_num):
    man = input().rstrip()
    listen_arr.add(man)

for _ in range(see_num):
    man = input().rstrip()
    see_arr.add(man)

listen_see_arr = listen_arr.intersection(see_arr)
listen_see_arr = sorted(listen_see_arr)

print(len(listen_see_arr))
print(*listen_see_arr, sep="\n")