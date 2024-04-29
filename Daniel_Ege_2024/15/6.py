for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((120 % A == 0) and (((x % A != 0) and (x % 18 == 0)) <= (x % 24 != 0))) == 0:
            can = False
    if can:
        print(A)