for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x | 42 > 64) and (x | 34 <= 102)) <= (not(x | A < 70))) == 0:
            can = False
    if can:
        print(A)