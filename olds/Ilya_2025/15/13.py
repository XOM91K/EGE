for A in range(0, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x + 2 * y > 48) or (y > x) or (x + 3 * y < A)) == 0:
                print(A)
                break