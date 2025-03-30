for A in range(1, 2000):
    can = True
    for x in range(1, 2000):
        if ((x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))) == 0:
            can = False
            break
    if can:
        print(A)