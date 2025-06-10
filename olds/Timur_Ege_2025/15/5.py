for A in range(1, 10000):
    k = 0
    for x in range(1, 10000):
        if (((x % 84 != 0) or (x % 90 != 0)) <= (x % A != 0)) == 1:
            k += 1
        else:
            break
    if k == 9999:
        print(A)