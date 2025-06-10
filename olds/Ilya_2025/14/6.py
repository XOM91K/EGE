for p in range(7, 100):
    for x in range(p):
        for y in range(p):
            c1 = 1 * p ** 2 + 6 * p + 1
            c2 = 5 * p ** 1 + 6
            c3 = 5 * p ** 3 + x * p ** 2 + y * p + 6
            if c1 * c2 == c3:
                print(p, y * p + x)
                exit()