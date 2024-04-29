for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % A == 0) or ((x % 23 == 0) <= (not(50 <= x <= 70)))) == False:
            can = False
    if can:
        print(A)
