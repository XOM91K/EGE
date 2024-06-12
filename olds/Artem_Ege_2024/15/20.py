for A in range(0, 1000):
    k = True
    for x in range(0, 300):
        for y in range(0, 300):
            if ((2 * x + y != 150) or (not(50 <= x <= 70)) or (A > y)) == 0:
                k = False
                break
    if k:
        print(A)