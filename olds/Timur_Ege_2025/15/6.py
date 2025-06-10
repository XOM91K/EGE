for A in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        if (((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (A <= x)) == 1:
            k += 1
        else:
            break
    if k == 999:
        print(A)