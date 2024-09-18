for A in range(0, 500):
    can = True
    for x in range(0, 500):
        for y in range(0, 500):
            if ((x * y > A) and (x > y) and (x < 8)) == 1:
                can = False
    if can:
        print(A)