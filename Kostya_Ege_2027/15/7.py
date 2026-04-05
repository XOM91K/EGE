for A in range(-1000, 1000):
    can = True
    for x in range(-1000, 1000):
        for y in range(-1000, 1000):
            if ((((A < x) or (x**2 - 7*x + 10 > 0)) and ((y**2 + 7*y + 12 > 0)) or (A >= y))) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)