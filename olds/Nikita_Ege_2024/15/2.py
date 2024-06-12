for A in range(1000):
    for x in range(1000):
        if ((x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))) == 0:
            break
    else:
        print(A)
        break