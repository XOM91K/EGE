for A in range(1, 300):
    can = True
    for x in range(1, 300):
        if ((x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))) == 0:
            can = False
    if can:
        print(A)