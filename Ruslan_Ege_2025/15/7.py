for A in range(0, 10000):
    ct_x = 0
    for x in range(0, 10000):
        if (((x not in range(5, 55)) and (x in range(50, 94))) <= (x > A)) == 0:
            ct_x += 1
    if ct_x == 20:
        print(A)