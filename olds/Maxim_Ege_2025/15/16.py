for A in range(-1000, 1000):
    k = 0
    for x in range(-1000, 1000):
        if (((not(5 <= x <= 54)) and (50 <= x <= 93)) <= (x > A)) == 0:
            k += 1
    if k == 20:
        print(A)