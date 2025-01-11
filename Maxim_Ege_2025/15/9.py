for a in range(0,100000):
    can = True
    for x in range(1,100000):
        if (((x & 7653 != 0) or (x & 9751 != 0)) <= (x & a > 0)) == 0:
            can = False
            break
    if can:
        print(a)