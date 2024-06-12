for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((not((x % 3 == 0) and (x % 5 == 0))) or (A >= 42 - x)) == 0:
            can = False
    if can:
        print(A)