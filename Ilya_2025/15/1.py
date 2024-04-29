for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y + 3 * x > A) or (x < 20) or (y < 50)) == 0:
                can = False
    if can:
        print(A)