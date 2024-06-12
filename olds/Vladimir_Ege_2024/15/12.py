for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x % 7 == 0) <= (x % 21 != 0)) or (2 * x + A >= 120)) == 0:
            can = False
    if can:
        print(A)