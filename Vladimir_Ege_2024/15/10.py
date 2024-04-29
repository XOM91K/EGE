for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x < A) or (y < A) or (x + 2 * y > 50)) == 0:
                can = False
    if can:
        print(A)