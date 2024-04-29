for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x & A != 0) <= ((x & 14 == 0) <= (x & 75 != 0))) == 0:
            can = False
    if can:
        print(A)