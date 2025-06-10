for A in range(1000):
    k = 0
    for x in range(1000):
        if ((x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))) == 1:
            k += 1
    if k == 1000:
        print(A)
        break