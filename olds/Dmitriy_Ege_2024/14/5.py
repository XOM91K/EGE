for p in range(7, 100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                c1 = y * p ** 2 + 3 * p + y
                c2 = y * p ** 2 + 6 * p + 5
                c3 = x * p ** 3 + 2 * p ** 2 + z * p
                if c1 + c2 == c3:
                    print(x * p ** 2 + y * p + z)