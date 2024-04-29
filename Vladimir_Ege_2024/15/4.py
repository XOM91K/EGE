for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if (((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)) == 0:
            flag = False
    if flag == True:
        print(A)