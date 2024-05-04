for A in range(1, 10000):
    can = True
    for x in range(1, 10000):
        if ((x & 2735 != 0) <= ((x & 1234 == 0) <= (x & A != 0))) == 0:
            can = False
            break
    if can:
        print(A)
