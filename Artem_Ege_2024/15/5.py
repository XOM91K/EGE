for A in range(1, 2000):
    for x in range(1, 2000):
        if (((x % 175 == 0) <= (x % 25 != 0)) or (2 * x+ A  >= 1780)) == 0:
            break
    else:
        print(A)