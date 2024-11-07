for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((((x % 10 == 0) and (x % 26 == 0)) and (x >= 300)) <= (A <= x)) == 0:
            flag = False
    if flag:
        print(A)