for p in range(8, 100):
    for x in range(p):
        for y in range(p):
            if (4 * p + 5) * (6 * p + 7) == (x * p ** 2 + y * p + 2):
                print(p, y * p + x)