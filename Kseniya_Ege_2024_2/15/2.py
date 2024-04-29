for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x & 13 != 0) and (x & 39 != 0)) <= ((x & A != 0) and (x & 13 != 0))) == 0:
            can = False
    if can:
        print(A)