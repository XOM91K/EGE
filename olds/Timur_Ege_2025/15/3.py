for A in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x >= 27) or (2 * x < 3 * y) or (A > (x + 2) * (y - 3))) == 1:
                k += 1
            else:
                break
    if k == 999 * 999:
        print(A)