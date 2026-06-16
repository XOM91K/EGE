for p in range(10, 100):
    for x in range(0, p):
        for y in range(0, p):
            for z in range(0, p):
                for w in range(0, p):
                    c1 = x * p ** 0 + 7 * p ** 1 + 0 * p ** 2 + y * p ** 3
                    c2 = z * p ** 0 + 9 * p ** 1 + y * p ** 2 + w * p ** 3
                    c3 = y * p ** 0 + x * p ** 1 + y * p ** 2 + x * p ** 3 + z * p ** 4
                    if c1 + c2 == c3 and x != y and x != z and x != w and y != w and y != z and z != w:
                        print(w * p ** 0 + z * p ** 1 + y * p ** 2 + x * p ** 3)