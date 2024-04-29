for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x % A == 0) and (31 <= x <= 68)) <= (x & 58 == 0)) == 0:
            can = False
    if can:
        print(A)