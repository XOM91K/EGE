for A in range(-1000, 1000):
    can = True
    for y in range(1, 1000):
        for x in range(1, 1000):
            if ((x < 25) <= ((x > 3 * y) <= (A > 4 * x * y))) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)