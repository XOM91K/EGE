for A in range(300):
    k = 0
    for x in range(300):
        for y in range(300):
            if ((7 * y + 5 * x < 1000) or (x < y) or (A < x)) == 1:
                k += 1
    if k == 300 * 300:
        print(A)