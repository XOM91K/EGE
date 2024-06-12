for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        if ((x & A != 0) or ((x & 52 == 0) and (x & 14 == 0))) == 0:
            can = False
    if can:
        print(A)