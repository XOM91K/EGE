for a in range(1, 100000):
    flag = 1
    for x in range(1, 100000):
        if (((x & 7653 != 0) or (x & 9751 != 0)) <= (x & a > 0)) == 0:
            flag = 0
            break
    if flag == 1:
        print(a)