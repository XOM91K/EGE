for A in range(1, 100000):
    can = True
    for x in range(1, 100000):
        if (((x % 2 == 0) <= (x % 13 != 0)) or ((x+A)>=1000))==0:
            can = False
            break
    if can == True:
        print(A)