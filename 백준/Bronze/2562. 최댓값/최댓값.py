arr = [int(input()) for _ in range(9)]

max_num = max(arr)
print(max_num)
print(arr.index(max_num)+1)