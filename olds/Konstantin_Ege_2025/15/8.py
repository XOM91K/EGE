for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        if (((x | 42 > 64) and (x | 34 <= 102)) <= (x | A >= 70)) == 0:
            can = False
            break
    if can == True:
        print(A)
