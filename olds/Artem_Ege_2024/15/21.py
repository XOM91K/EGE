for A in range(0, 500):
    k = True
    for x in range(0, 500):
        for y in range(0, 500):
            if ((2 * x + y != 150) or (not(50 <= x <= 70)) or (A > y)) == 0:
                k = False
    if k:
        print(A)