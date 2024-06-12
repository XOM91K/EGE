for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((2 * x >= 2 * A + 3 * y) or (y < 5) or (y >= 18) or (x < 87)) == 0:
                can = False
                break
    if can == True:
        print(A)