for p in range(10, 30):
    for x in range(p):
        for y in range(p):
            c1 = 5 * p ** 3 + x * p ** 2 + 8 * p + 3
            c2 = x * p ** 3 + 9 * p ** 2 + x * p + 9
            c3 = y * p ** 3 + 2 * p ** 2 + y
            if c1 + c2 == c3:
                print(x * p ** 3 + y * p ** 2 + y * p + x)