for A in range(1, 20000):
    can = True
    for x in range(1, 20000):
        if (((x & 7653 != 0) or (x & 9751 != 0)) <= (x & A > 0)) == 0:
            can = False
    if can:
        print(A)