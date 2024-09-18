for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x & 123 != 0) or (x & 98 != 0)) <= ((x & 75 == 0) <= (x & A != 0))) == 0:
            can = False
    if can:
        print(A)
        break