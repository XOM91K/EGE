for A in range(1, 100000):
    can = True
    for x in range(1, 100000):
        if (((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (A <= x)) == 0:
            can = False
            break
    if can:
        print(A)