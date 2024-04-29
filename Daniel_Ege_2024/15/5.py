for A in range(1000):
    can = True
    for x in range(1000):
        for y in range(1000):
            if ((x >= 27) or (2 * x < 3 * y) or (A > (x + 2) * (y - 3))) == 0:
                can = False
    if can:
        print(A)