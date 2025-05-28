for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x % 13 == 0) <= (x not in range(40, 61))) or (A < x + 20)) == 0:
            can = False
    if can:
        print(A)