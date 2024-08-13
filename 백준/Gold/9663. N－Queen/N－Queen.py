n = int(input())
rows = [0] * (n+1)
cnt = 0

def is_not_attack(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == abs(x - i):
            return False
    return True

def n_queens(idx=0):
    global cnt
    if idx == n:
        cnt += 1
        return

    for i in range(n):
        rows[idx] = i
        if is_not_attack(idx):
            n_queens(idx + 1)

n_queens()

print(cnt)