for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((11 <= y) or (7 * y < x) or (A > x * y)) == 0:
                can = False
                break
    if can:
        print(A)