for a in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x % 2 == 0) <= (x % 13 != 0)) or (x + a >= 1000)) == 0:
            can = False
    if can:
        print(a)
