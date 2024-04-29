for A in range(1, 1000):
    k = True
    for x in range(1, 1000):
        if ((160 <= x <= 180) <= ((x % 35 == 0) <= (x % A == 0))) == 0:
            k = False
    if k:
        print(A)
