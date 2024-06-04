for A in range(1, 1000):
    k = True
    for x in range(1, 1000):
        if (not((x % 3 == 0) and (x % 5 == 0)) or (A >= 42 - x)) == 0:
            k = False
    if k:
        print(A)
