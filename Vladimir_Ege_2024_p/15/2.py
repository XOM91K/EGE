for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % 33 == 0) <= ((x % A != 0) <= (x % 242 != 0))) == 0:
            can = False
    if can:
        print(A)