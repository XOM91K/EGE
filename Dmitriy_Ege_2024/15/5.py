for A in range(1, 5000):
    can = True
    for x in range(1, 5000):
        if (((x % 175 == 0) <= (x % 25 != 0)) or ((2 * x + A) >= 1780)) == False:
            can = False
    if can == True:
        print(A)
        break