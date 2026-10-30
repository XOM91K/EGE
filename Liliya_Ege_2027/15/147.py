for A in range(1, 1000):
    can = True # A = 1 x = 35
    for x in range(1, 1000):
        if ((A + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0))) == 0:
            can = False
            break
    if can == True:
        print(A)
