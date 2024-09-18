for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((7*y + 5*x<1000) or (x < y) or (A < x)) == 0:
                can = False
    if can:
        print(A)