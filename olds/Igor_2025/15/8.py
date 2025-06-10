for A in range(0, 100000):
    can = True
    for x in range(0, 100000):
        if (((x & 5160 > 0) or (x & 3650 > 0)) <= ((x & 9545 == 0) <= (x & A > 0))) == 0:
            can = False
            break
    if can:
        print(A)
        break