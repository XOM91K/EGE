for A in range(1, 1000):
    f = True
    if A != 21 and A != 40:
        for x in range(1, 1000):
            if (((x % (A - 21) == 0) and (x % (40 - A) == 0)) <= (x % 90 == 0)) == 0:
                f = False
        if f:
            print(A)
