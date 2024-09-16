n = int(input()) 
str_list = list(input()) 

result = 0 
for i in range(n):
    result += ((ord(str_list[i]) - 96) * (31 ** i))

print(result % 1234567891)