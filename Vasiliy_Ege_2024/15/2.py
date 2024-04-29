for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)) == 0:
            can = False
    if can:
        print(A)