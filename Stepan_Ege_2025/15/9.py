for A in range(1, 10000):
    can = True
    for x in range(1, 10000):
        if (((x % 84 != 0) or (x % 90 != 0)) <= (x % A != 0)) == 0:
            can = False
            break
    if can:
        print(A)