for A in range(0, 10000000):
    can = True
    for x in range(0, 100):
        for y in range(0, 100):
            if ((680 * y + 256 * x < A) or (5 * x + 3 * y > 11111)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)