for a in range(0, 1000):
    can = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x % a == 0) <= (((x % 55 != 0)) <= ((y % 101 != 0)))) == 0:
                can = False
                break
        if can == False:
            break

    if can:
        print(a)