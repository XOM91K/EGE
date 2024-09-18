for p in range(10, 500):
    for x in range(p):
        for y in range(p):
            c1 = 1 * p ** 3 + 7 * p ** 2 + x * p ** 1 + 8 * p ** 0
            c2 = y * p ** 3 + x * p ** 2 + y * p ** 1 + 6 * p ** 0
            c3 = 9 * p ** 3 + y * p ** 2 + x * p ** 1 + 0 * p ** 0
            if c1 + c2 == c3:
                print(x * p ** 2 + x * p ** 1 + y * p ** 0)