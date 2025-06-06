for p in range(10, 100):
    for x in range(0, p):
        for y in range(0, p):
            for z in range(0, p):
                for w in range(0, p):
                    if x != y and x != z and x != w and y != z and y != w and z != w:
                        c1 = y * p ** 3 + 7 * p ** 1 + x
                        c2 = w * p ** 3 + y * p ** 2 + 9 * p + z
                        c3 = z * p ** 4 + x * p ** 3 + y * p ** 2 + x * p ** 1 + y
                        if c1 + c2 == c3:
                            print(x, y, z, w)
                            print(x * p ** 3 + y * p ** 2 + z * p + w)