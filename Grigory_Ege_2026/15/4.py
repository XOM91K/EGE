for A in range(-100, 100):
    can = True
    for x in range(-100, 100):
        for y in range(-100, 100):
            if (((A < x) or (x ** 2 - 7 * x + 10 > 0)) and ((A >= y) or (y ** 2 + 7 * y + 12 > 0))) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)