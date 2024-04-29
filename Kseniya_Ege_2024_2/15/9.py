for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        if (((x & 52 != 0) and (x & 36 == 0)) <= (x & A != 0)) == 0:
            can = False
    if can:
        print(A)