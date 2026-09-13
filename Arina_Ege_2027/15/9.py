for a in range(20000):
    can = True
    for x in range(20000):
        if (((x & 7653 != 0) or (x & 9751 != 0)) <= (x & a > 0)) == 0:
            can = False
            break
    if can:
        print(a)
        break