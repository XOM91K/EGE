for p in range(7,36):
    for x in range(p):
        for y in range(p):
            c1 = '161'
            c2 = '56'
            v1 = '5' + str(x) + str(y) + '6'
            h = int(c1, p) * int(c2, p)
            i = int(v1, p)
            if h == i:
                print(str(y) + str(x))