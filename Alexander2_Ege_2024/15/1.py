for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if A != 40 and A != 21:
            if (((x % (A - 21) == 0) and (x % (40 - A) == 0)) <= (x % 90 == 0)) == 0:
                can = False
    if can:
        print(A)