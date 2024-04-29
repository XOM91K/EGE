for p in range(9, 100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                c1 = y * p ** 2 + 2 * p + y
                c2 = y * p ** 2 + 8 * p + 7
                c3 = 1 * p ** 3 + x * p ** 2 + z * p + z
                if c1 + c2 == c3:
                    print(x * p ** 2 + y * p + z)