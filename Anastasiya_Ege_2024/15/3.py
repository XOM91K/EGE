for a in range(1000, -1, -1):
    for x in range(0, 300):
        for y in range(0, 300):
            if ((4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < a)) == 0:
                print(a)