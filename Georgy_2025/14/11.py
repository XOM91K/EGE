for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((5 < y) or (x > 32) or (x + 2 * y < A)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)
        break