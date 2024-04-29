for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x & 2735 != 0) <= ((x & 1234 == 0) <= (x & A != 0))) == 0:
             can = False
    if can:
        print(A)