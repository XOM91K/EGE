for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x > A) or (y > A) or (y - 2 * x + 12 != 0)) == 0:
                can = False
                break
    if can:
        print(A)
