for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((2*x + 3*y) != 150) or (x < A) and (y < A)) == 0:
                can = False
    if can:
        print(A)
#7