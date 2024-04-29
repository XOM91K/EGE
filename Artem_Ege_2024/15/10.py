for A in range(0, 300):
    c = True
    for x in range(0, 300):
        for y in range(0, 300):
            if ((7 * y + 5 * x < 1000) or (x < y) or (A < x)) == 0:
                c = False
    if c:
        print(A)