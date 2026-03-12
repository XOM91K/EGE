for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y > A) or (152 != 2 * y + 3 * x) or (A < x)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)
