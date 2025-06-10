for d in range(1, 1000000):
    if d % 2 == 0 and len(str(d)) == 4:
        print(d, 'Четное и четырёхзначное')
    elif d % 2 != 0 and len(str(d)) == 4:
        print(d, 'Нечетное и четырёхзначное')