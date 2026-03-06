for p in range(10, 100):
    for x in range(0, p):
        for y in range(0, p):
            for z in range(0, p):
                for w in range(0, p):
                    a = y * p ** 3 + 0 * p ** 2 + 7 * p ** 1 + x * p ** 0
                    b = w * p ** 3 + y * p ** 2 + 9 * p ** 1 + z * p ** 0
                    c = z * p ** 4 + x * p ** 3 + y * p ** 2 + x * p ** 1 + y * p ** 0
                    if a + b == c and len(set([x, y, z, w])) == 4:
                        print(p, x * p ** 3 + y * p ** 2 + z * p ** 1 + w * p ** 0)
