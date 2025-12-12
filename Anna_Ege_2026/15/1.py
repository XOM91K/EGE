for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((2 * x + y != 110) or (x < y) or (A < x)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)