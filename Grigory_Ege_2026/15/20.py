for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % 332 == 0) <= ((x % A != 0) <= (x % 412 != 0))) == 0:
            can = False
            break
    if can:
        print(A)