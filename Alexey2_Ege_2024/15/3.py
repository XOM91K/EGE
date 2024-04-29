for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x + 2 * y > A) or (y < x) or (x < 30)) == 0:
                can = False
    if can:
        print(A)