for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        if ((x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))) == 0:
            can = False
    if can:
        print(A)