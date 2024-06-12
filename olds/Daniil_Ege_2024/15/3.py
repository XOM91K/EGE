for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        if ((x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))) == 0:
            can = False
    if can == True:
        print(A)
        break