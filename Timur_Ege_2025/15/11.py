for p in range(8, 100):
    for x in range(0, p):
        for y in range(0, p):
            c1 = 1 * p ** 3 + x * p ** 2 + 7 * p ** 1 + 7 * p ** 0
            c2 = x * p ** 3 + x * p ** 2 + 7 * p ** 1 + 7 * p ** 0
            c3 = y * p ** 3 + 0 * p ** 2 + y * p ** 1 + y * p ** 0
            if c1 + c2 == c3:
                print(y * p ** 3 + x * p ** 2 + y * p ** 1 + x * p ** 0)