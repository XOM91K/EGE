for p in range(9, 100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (y * p ** 2 + 2 * p + y) + (y * p ** 2 + 8 * p + 7) == 1 * p ** 3 + x * p ** 2 + z * p + z:
                    print(x * p ** 2 + y * p + z)