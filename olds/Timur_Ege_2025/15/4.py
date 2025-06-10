for A in range(-100,100):
    k = 0
    for x in range(-100,100):
        for y in range(-100,100):
            if (((A < x) or ( x ** 2 - 7 * x + 10 > 0)) and ((A >= y) or (y ** 2 + 7 * y + 12 > 0))) == 1:
                k += 1
            else:
                break
    if k == 200 * 200:
        print(A)