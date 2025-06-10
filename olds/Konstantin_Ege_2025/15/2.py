for A in range(1, 1000):
    for x in range(1, 1000):
        if not(((x & 13 != 0) and (x & 39 != 0)) <= ((x & A != 0) and (x & 13 != 0))):
            break
    else:
        print(A)