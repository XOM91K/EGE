for A in range(-500, 500):
    k = True
    for x in range(-500, 500):
        for y in range(-500, 500):
            if (((A < x) or (x ** 2 - 7 * x + 10 > 0)) and ((A >= y) or (y ** 2 + 7 * y + 12 > 0))) == 0:
                k = False
                break
        if k == False:
            break
    if k:
        print(A)