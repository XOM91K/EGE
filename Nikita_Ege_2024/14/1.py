for p in range(9, 100):
    for y in range(0, p):
        for x in range(0, p):
            for z in range(0, p):
                if (y * p ** 2 + 2 * p + y) + (y * p ** 2 + 8 * p + 7) == 1 * p ** 3 + x * p ** 2 + z * p + z:
                    print(x * p ** 2 + y * p + z)