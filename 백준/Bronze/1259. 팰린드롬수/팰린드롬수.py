while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num == int(str(num)[::-1]):
            print('yes')
        else:
            print('no')