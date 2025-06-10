for x in range(1, 1000):
    if (((x - 1) * (3 * x - 1)) * 2) + ((x - 1) * (x + 1)) > 200_000:
        print(x)