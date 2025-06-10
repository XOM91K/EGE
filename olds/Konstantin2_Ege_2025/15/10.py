for A in range(1,1000):
    can = True
    for x in range(1,1000):
        if (((405 % x == 0) <= (81 % x == 0)) or (A -x > 162)) == 0:
            can = False
            break
    if can:
        print(A)