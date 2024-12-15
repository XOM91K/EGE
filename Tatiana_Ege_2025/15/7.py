for A in range(300, 1, -1):
    for x in range(300):
        for y in range(300):
            if ((x + 2 * y > 48) or (y > x) or (x + 3 * y < A)) == 0:
                print(A)
                exit()