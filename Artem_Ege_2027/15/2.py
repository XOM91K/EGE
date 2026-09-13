for A in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        if (((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)) == 1:
            k += 1
    if k == 999:
        print(A)