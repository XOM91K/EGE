for A in range(0, 1000):
    ct = 0
    for x in range(0, 1000):
        if (((not(5 <= x <= 54)) and (50 <= x <= 93)) <= (x > A)) == 0:
            ct += 1
    if ct == 20:
        print(A)
