import sys
input = sys.stdin.readline
pocket_num, q_num = map(int, input().split())

pocketmon_dic = {}
reverse_pocketmon_dic = {}

for idx in range(1, pocket_num + 1):
    name = input().strip()
    pocketmon_dic[idx] = name
    reverse_pocketmon_dic[name] = str(idx)

for _ in range(q_num):
    question = input().strip()
    if question.isdigit():
        print(pocketmon_dic[int(question)])
    else:
        print(reverse_pocketmon_dic[question])