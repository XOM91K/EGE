for A in range(1, 1500):
    can = True
    for x in range(1, 1500):
        if (((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (A <= x)) == 0:
            can = False
    if can:
        print(A)