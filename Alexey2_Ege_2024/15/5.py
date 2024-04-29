for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % A == 0) or ((70 <= x <= 80) <= (x % 18 != 0))) == 0:
            can = False
    if can == True:
        print(A)