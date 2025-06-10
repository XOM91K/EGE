for A in range(300):
    can = True
    for x in range(300):
        for y in range(300):
            if ((7 * y + 5 * x < 1000) or (x < y) or (A < x)) == 0:
                can = False
    if can:
        print(A)