for x in range(1, 1000):
    for y in range(1, 1000):
        if x * 2 + y == 1000:
            if (x + y * 2) - (y * 2) == 363:
                print(x)