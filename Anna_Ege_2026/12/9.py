for x in range(501):
    for y in range(999):
        if ((x + (y * 2) + 200) == x * 3) and x * 2 + y == 1000:
            print(y)