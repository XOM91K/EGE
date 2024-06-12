for A in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        if ((x & 41 == 0) <= ((x & 119 != 0) <= (x & A != 0))) == 1:
            k += 1
        if k == 999:
            print(A, k)
