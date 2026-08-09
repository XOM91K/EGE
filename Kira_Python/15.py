for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x >= 27) or (2 * x < 3 * y) or (A > (x + 2) * (y - 3))) == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)