for A in range(1000):
    can = True
    for x in range(1000):
        if (((x & 57 > 0) or (x & 99 > 0)) <= (x & A > 0)) == 0:
            can = False
    if can:
        print(A)