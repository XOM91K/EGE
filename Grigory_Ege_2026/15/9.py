for A in range(0, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((3 * x + y > 48) or (x > y) or (4 * x + y < A)) == 0:
                print(A)