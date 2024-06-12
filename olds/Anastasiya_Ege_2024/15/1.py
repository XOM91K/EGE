for a in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((((x % 12 == 0) or (x % 36 == 0)) <= (x % a == 0)) and (a ** 2 - a - 90 < 0)) == 0:
            can = False
    if can == True:
        print(a)