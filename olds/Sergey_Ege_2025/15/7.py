for A in range(0, 500):
    for x in range(0, 500):
        for y in range(0, 500):
            if ((3 * x + 2 * y > 95) or (4 * x < 3 * y) or (x + 4 * y < A)) == 0:
                print(A)