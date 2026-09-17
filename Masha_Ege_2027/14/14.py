for p in range(10, 30):
    for x in range(0, p):
        for y in range(0, p):
            for z in range(0, p):
                for w in range(0, p):
                    if len(set([x, y, z, w])) == 4:
                        c1 = y * p ** 3 + 7 * p + x
                        c2 = w * p ** 3 + y * p ** 2 + 9 * p + z
                        c3 = z * p ** 4 + x * p ** 3 + y * p ** 2 + x * p + y
                        if (c1 + c2) == c3:
                            print(x * p ** 3 + y * p ** 2 + z * p ** 1 + w )
