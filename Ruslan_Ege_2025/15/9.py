for A in range(1, 10000):
    can = True
    for x in range(1, 10000):
        if (((x % 3 == 0) <= (x % 2 != 0)) or (x - A >= 4)) == 0:
            can = False
            break
    if can:
        print(A)