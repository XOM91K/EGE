for p in range(10, 100):
    for x in range(0, p):
        for y in range(0, p):
            c1 = 5 * p ** 3 + x * p ** 2 + 8 * p ** 1 + 3 * p ** 0
            c2 = x * p ** 3 + 9 * p ** 2 + x * p ** 1 + 9 * p ** 0
            c3 = y * p ** 3 + 2 * p ** 2 + 0 * p ** 1 + y * p ** 0
            if c1 + c2 == c3:
                print(x * p ** 3 + y * p ** 2 + y * p ** 1 + x * p ** 0)