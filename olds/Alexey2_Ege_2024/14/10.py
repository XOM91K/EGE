for p in range(7, 100):
    for x in range(p):
        for y in range(p):
            d1 = 3 * p + 4
            d2 = 5 * p + 6
            d3 = x * p ** 2 + y * p + 2
            if d1 * d2 == d3:
                print(y * p + x)