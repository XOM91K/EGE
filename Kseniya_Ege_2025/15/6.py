for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((2 * x - 4 * y < A) or (y >= x) or (x > 67)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)