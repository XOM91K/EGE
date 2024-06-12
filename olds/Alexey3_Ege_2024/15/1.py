for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))) == 0:
            flag = False
        if flag:
            print(A)