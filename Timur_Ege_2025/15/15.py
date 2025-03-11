for A in range(1,1000):
    can = True
    for x in range(1,1000):
        if (((x % 3 == 0) <= (x % 17 != 0)) or (A >= 190 - x)) == 0:
            can = False
            break
    if can:
        print(A)