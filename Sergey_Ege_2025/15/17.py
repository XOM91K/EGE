for A in range(1, 10000):
    can = True
    for x in range(1, 10000):
        if (((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40)) == 0:
            can = False
            break
    if can:
        print(A)