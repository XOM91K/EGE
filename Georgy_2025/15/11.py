for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (x == A or (10 >= x >= 40) or (x%6!=0)) == 0:
            can = False
    if can:
        print(A)