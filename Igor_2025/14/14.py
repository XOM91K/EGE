for p in range(30):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    c1 = y * p ** 3 + 2 * p ** 2 + 7 * p ** 1 + x
                    c2 = w * p ** 3 + y * p ** 2 + 8 * p ** 1 + 6
                    c3 = x * p ** 4 + x * p ** 3 + z * p ** 2 + 3 * p ** 1 + y
                    if c1 + c2 == c3:
                        print(x * p ** 3 + y * p ** 2 + z * p ** 1 + w)
