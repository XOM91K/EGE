for A in range(1, 150000):
    for x in range(1, 150000):
        if ((x & 27358 != 0) <= ((x & 12345 == 0) <= (x & A != 0))) == 0:
            break
    else:
        print(A)
        break