for A in range(1, 1000):
    f = 1
    for x in range(1, 1000):
        if (((405 % x == 0) <= (81 % x == 0)) or (A - x > 162)) == 0:
            f = 0
            break

    if f:
        print(A)