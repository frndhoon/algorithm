DIVIDE_NUM = 42
COUNT = 10

diff_remain = set()

for _ in range(COUNT):
    num = int(input())
    diff_remain.add(num % DIVIDE_NUM)

print(len(diff_remain))
