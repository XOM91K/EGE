for r in range(10, 100):
    for x in range(0, r):
        for y in range(0, r):
            c1 = 5 * r ** 3 + x * r ** 2 + 8 * r + 3
            c2 = x * r ** 3 + 9 * r ** 2 + x * r + 9
            c3 = y * r ** 3 + 2 * r ** 2 + y
            if c1 + c2 == c3:
                print(x * r ** 3 + y * r ** 2 + y * r + x)