for p in range(9, 1000):
    for x in range(0, p):
        for y in range(0, p):
            c1 = 7 * p + 5
            c2 = 8 * p + 7
            c3 = 1 * p ** 3 + x * p ** 2 + y * p + 2
            if c1 * c2 == c3:
                print(y * p + x)