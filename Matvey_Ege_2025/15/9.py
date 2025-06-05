for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x % A == 0) <= ((x % 55 != 0) <= (y % 101 != 0))) == 0:
                can = False
                break
        if not can:
            break
    if can:
        print(A)