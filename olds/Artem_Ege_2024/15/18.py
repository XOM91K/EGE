for A in range(1, 1000):
    k = True
    for x in range(1, 1000):
        if ((x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))) == 0:
            k = False
    if k:
        print(A)