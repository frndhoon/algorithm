while True:
    width, height, hypotenuse = sorted(list(map(int, input().split())))

    if width == 0 and height == 0 and hypotenuse == 0:
        break

    if (width ** 2) + (height ** 2) == (hypotenuse ** 2):
        print("right")
    else:
        print("wrong")