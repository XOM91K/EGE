for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % A == 0) or ((60 <= x <= 80) <= (x % 22 != 0))) == 0:
            can = False
            break
    if can == True:
        print(A)