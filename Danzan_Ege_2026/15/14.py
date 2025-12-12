for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((y < 4) or (x >= 20) or ((3*x + y) > A)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)