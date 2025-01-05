for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < A)) == 0:
                print(A)
                can = False
                break
        if can == False:
            break