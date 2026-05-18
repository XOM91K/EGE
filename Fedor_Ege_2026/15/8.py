for a in range(1000,0,-1):
    cn = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y > a) or (152 != 2 * y + 3 * x) or (x > a)) == 0:
                cn = False
                break
        if cn == False:
            break
    if cn:
        print(a)