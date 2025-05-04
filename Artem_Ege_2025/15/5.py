for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x ** 2 + y ** 2 > 1024 - x) or (y < -2 * x + A)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)