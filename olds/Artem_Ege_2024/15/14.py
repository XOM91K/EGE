for A in range(1, 1000):
    k = True
    for x in range(1, 1000):
        if ((x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))) == 0:
            k = False
    if k:
        print(A)