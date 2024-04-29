for p in range(8, 100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                c1 = y * p ** 2 + 2 * p + y
                c2 = y * p ** 2 + 5 * p + 7
                c3 = x * p ** 3 + z * p ** 2 + z * p + 3
                if c1 + c2 == c3:
                    print(p, x * p ** 2 + y * p + z)