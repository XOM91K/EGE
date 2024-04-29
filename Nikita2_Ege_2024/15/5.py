for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % A == 0) or (not((x % 17 == 0) and (x % 23 == 0)))) == 0:
            can = False
    if can:
        print(A)