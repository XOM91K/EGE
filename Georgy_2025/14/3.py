for p in range(8, 100):
    for x in range(p):
        for y in range(p):
            c1 = 1 * p ** 3 + x * p ** 2 + 7 * p + 7
            c2 = x * p ** 3 + x * p ** 2 + 7 * p + 7
            c3 = y * p ** 3 + 0 + y * p + y
            if c1 + c2 == c3:
                print(y * p ** 3 + x * p ** 2 + y * p + x)