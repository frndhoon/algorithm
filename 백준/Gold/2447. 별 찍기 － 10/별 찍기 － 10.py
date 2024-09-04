N = int(input())


def take_a_star(num):
    if num == 1:
        return ['*']

    stars = take_a_star(num // 3)
    lst = []

    for star in stars:
        lst.append(star * 3)
    for star in stars:
        lst.append(star+' '*(num//3)+star)
    for star in stars:
        lst.append(star * 3)
    return lst

star = take_a_star(N)

print('\n'.join(star))