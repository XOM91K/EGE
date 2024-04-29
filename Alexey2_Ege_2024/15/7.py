for A in range(1, 100000):
    can = True
    for x in range(1, 100000):
        if (((x & 8375 != 0) or (x & 6743 != 0)) <= (x & A > 0)) == 0:
            can = False
            break
    if can == True:
        print(A)
        break