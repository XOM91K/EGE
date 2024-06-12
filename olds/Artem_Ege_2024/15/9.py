for A in range(1, 2000):
    c = True
    for x in range(1, 1000):
        if ((x % A == 0) and (A < 10) or (x % 44 != 0) and (x % 99 != 0) and (A < 10)) == 0:
            c = False
    if c:
        print(A)