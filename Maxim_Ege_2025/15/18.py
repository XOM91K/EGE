for A in range(-1000,1000):
    can = True
    for x in range(1,1000):
        for y in range(1,1000):
            if ((x*y > A) and (x > y) and (x < 8)) == 1:
                can = False
        if can == False:
            break
    if can:
        print(A)
        break