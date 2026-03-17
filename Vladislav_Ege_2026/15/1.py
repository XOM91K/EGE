for A in range(88, 10000):
    can = True
    for x in range(1, 10000):
        if ((A + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0))) == 0:
            can = False
    if can == True:
        print(A)