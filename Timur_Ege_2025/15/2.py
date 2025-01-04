for A in range(1, 100000):
    k = 0
    for x in range(1, 100000):
        if (((x & 7653 != 0) or (x & 9751 != 0)) <= (x & A > 0)) == 1:
            k += 1
        else:
            break
    if k == 99999:
        print(A)