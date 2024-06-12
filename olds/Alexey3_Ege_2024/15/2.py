for A in range(5000):
    can = True
    for x in range(5000):
        for y in range(5000):
            if ((2 * x + y != 150) or (not(50 <= x <= 70)) or (A > y)):
                can = False
                break
        if can == False:
            break
    if can:
        print(A)